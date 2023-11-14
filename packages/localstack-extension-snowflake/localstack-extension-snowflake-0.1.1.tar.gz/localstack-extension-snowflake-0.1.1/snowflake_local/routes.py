_L='precision'
_K='location'
_J='VARIANT'
_I='type'
_H='value'
_G='data'
_F='status_code'
_E='test'
_D='name'
_C='success'
_B='POST'
_A=True
import base64,gzip,json,logging,os.path,re
from typing import Any
import pyarrow,pyarrow.json
from localstack.aws.connect import connect_to
from localstack.http import Request,Response,route
from localstack.utils.aws.resources import get_or_create_bucket
from localstack.utils.strings import to_str
from localstack_ext.services.rds.engine_postgres import get_type_name
from snowflake_local.config import ASSETS_BUCKET_NAME,ASSETS_KEY_PREFIX
from snowflake_local.constants import PATH_QUERIES,PATH_SESSION,PATH_V1_STREAMING
from snowflake_local.encodings import get_parquet_from_blob
from snowflake_local.models import QueryResponse
from snowflake_local.queries import execute_query,insert_rows_into_table
from snowflake_local.storage import FileRef,StageType
LOG=logging.getLogger(__name__)
REGEX_FILE_FORMAT='\\s*(CREATE|DROP)\\s+.*FILE\\s+FORMAT\\s+(?:IF\\s+NOT\\s+EXISTS\\s+)?(.+)(\\s+TYPE\\s+=(.+))?'
TMP_UPLOAD_STAGE='@tmp-stage-internal'
ENCRYPTION_KEY=_E
class RequestHandler:
	@route(PATH_SESSION,methods=[_B])
	def session_request(self,request,**B):
		if request.args.get('delete')=='true':LOG.info('Deleting session data...')
		A={_C:_A};return Response.for_json(A,status=200)
	@route(f"{PATH_SESSION}/v1/login-request",methods=[_B])
	def session_login(self,request,**B):A={_G:{'nextAction':None,'token':'token123','masterToken':'masterToken123','parameters':[{_D:'AUTOCOMMIT',_H:_A}]},_C:_A};return Response.for_json(A,status=200)
	@route(f"{PATH_QUERIES}/query-request",methods=[_B])
	def start_query(self,request,**H):
		B=_get_data(request);E=B.get('sqlText','');F=B.get('bindings',{});C=[]
		for G in range(1,100):
			D=F.get(str(G))
			if not D:break
			C.append(D.get(_H))
		A=handle_query_request(E,C);A=A.to_dict();return Response.for_json(A,status=200)
	@route(f"{PATH_QUERIES}/abort-request",methods=[_B])
	def abort_query(self,request,**A):return{_C:_A}
	@route(f"{PATH_V1_STREAMING}/client/configure",methods=[_B])
	def streaming_configure_client(self,request,**D):A=FileRef.parse(TMP_UPLOAD_STAGE);B=_get_s3_location(A);C={_C:_A,_F:0,'prefix':_E,'deployment_id':_E,'stage_location':B,_G:{}};return C
	@route(f"{PATH_V1_STREAMING}/channels/open",methods=[_B])
	def streaming_open_channel(self,request,**G):E='BINARY';D='variant';C='logical_type';B='physical_type';F=_get_data(request);A={_C:_A,_F:0,'client_sequencer':1,'row_sequencer':1,'encryption_key':ENCRYPTION_KEY,'encryption_key_id':123,'table_columns':[{_D:'record_metadata',_I:D,B:E,C:_J},{_D:'record_content',_I:D,B:E,C:_J}],_G:{}};A.update(F);return A
	@route(f"{PATH_V1_STREAMING}/channels/status",methods=[_B])
	def streaming_channel_status(self,request,**B):A={_C:_A,_F:0,'message':'test channel','channels':[{_F:0,'persisted_row_sequencer':1,'persisted_client_sequencer':1,'persisted_offset_token':'1'}]};return A
	@route(f"{PATH_V1_STREAMING}/channels/write/blobs",methods=[_B])
	def streaming_channel_write_blobs(self,request,**S):
		G='blobs';H=_get_data(request);I=FileRef.parse(TMP_UPLOAD_STAGE);J=_get_s3_location(I)[_K];D=[]
		for A in H.get(G,[]):
			B=A.get('path')or'/';K=B if B.startswith('/')else f"/{B}";L=J+K;M,T,N=L.partition('/');O=connect_to().s3;C=O.get_object(Bucket=M,Key=N);P=C['Body'].read()
			try:Q=get_parquet_from_blob(P,key=ENCRYPTION_KEY,blob_path=B)
			except Exception as R:LOG.warning('Unable to parse parquet from blob: %s - %s',A,R);continue
			E=A.get('chunks')or[]
			if not E:LOG.info('Chunks information missing in incoming blob: %s',A)
			for F in E:insert_rows_into_table(table=F['table'],database=F['database'],rows=Q)
			D.append({})
		C={_C:_A,_F:0,G:D};return C
	@route('/telemetry/send/sessionless',methods=[_B])
	def send_telemetry_sessionless(self,request,**B):A={_C:_A,_G:{}};return A
def handle_query_request(query,params):
	B=query;A=QueryResponse();A.data.parameters.append({_D:'TIMEZONE',_H:'UTC'});B=B.strip(' ;');H=re.match('^\\s*PUT\\s+.+',B,flags=re.IGNORECASE)
	if H:return handle_put_file_query(B,A)
	I=re.match('^\\s*CREATE\\s+WAREHOUSE\\s.+',B,flags=re.IGNORECASE)
	if I:return A
	J=re.match('^\\s*USE\\s.+',B,flags=re.IGNORECASE)
	if J:return A
	K=re.match('^\\s*CREATE\\s+STORAGE\\s.+',B,flags=re.IGNORECASE)
	if K:return A
	L=re.match('^\\s*COPY\\s+INTO\\s.+',B,flags=re.IGNORECASE)
	if L:return A
	M=re.match(REGEX_FILE_FORMAT,B,flags=re.IGNORECASE)
	if M:return A
	C=execute_query(B,params)
	if C and C._context.columns:
		D=[];N=C._context.columns
		for O in C:D.append(list(O))
		F=[]
		for E in N:F.append({_D:E[_D],_I:get_type_name(E['type_oid']),'length':E['type_size'],_L:0,'scale':0,'nullable':_A})
		A.data.rowset=D;A.data.rowtype=F;A.data.total=len(D)
	G=re.match('.+FROM\\s+@',B);A.data.queryResultFormat='arrow'if G else'json'
	if G:A.data.rowsetBase64=_to_pyarrow_table_bytes_b64(A);A.data.rowset=[];A.data.rowtype=[]
	return A
def _to_pyarrow_table_bytes_b64(result):
	I='16777216';B=result;J={'byteLength':I,'charLength':I,'logicalType':_J,_L:'38','scale':'0','finalType':'T'};D=[];E=[A[_D].replace('_col','$')for A in B.data.rowtype]
	for K in range(len(E)):L=[A[K]for A in B.data.rowset];D.append(pyarrow.array(L))
	F=pyarrow.record_batch(D,names=E);G=pyarrow.BufferOutputStream();A=F.schema
	for C in range(len(A)):H=A.field(C);M=H.with_metadata(J);A=A.set(C,M);H=A.field(C)
	with pyarrow.ipc.new_stream(G,A)as N:N.write_batch(F)
	B=base64.b64encode(G.getvalue());return to_str(B)
def handle_put_file_query(query,result):
	A=result;D=re.match('^PUT\\s+(\\S+)\\s+(\\S+)',query);B=D.group(1);C=D.group(2);B=B.removeprefix('file://')
	if'/'not in C:C=f"{C}/{os.path.basename(B)}"
	E=FileRef.parse(C);A.data.command='UPLOAD';A.data.src_locations=[B];A.data.stageInfo=_get_s3_location(E);A.data.sourceCompression='none';return A
def _get_s3_location(file_ref):
	A=file_ref;B=A.get_path().lstrip('/');get_or_create_bucket(ASSETS_BUCKET_NAME,s3_client=connect_to().s3);C=f"{ASSETS_BUCKET_NAME}/{ASSETS_KEY_PREFIX}"
	if A.stage.stage_type==StageType.USER:D=f"{C}{B}"
	else:D=f"{C}{os.path.dirname(B)}"
	return{'locationType':'S3','region':'us-east-1','endPoint':'s3.localhost.localstack.cloud:4566',_K:D,'creds':{'AWS_KEY_ID':_E,'AWS_SECRET_KEY':_E}}
def _get_data(request):
	A=request.data
	if isinstance(A,bytes):
		try:A=gzip.decompress(A)
		except gzip.BadGzipFile:pass
		A=json.loads(to_str(A))
	return A