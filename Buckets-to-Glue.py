import boto3
from pyspark.sql.functions import *
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
s3 = boto3.resource('s3')
datasource0 = glueContext.create_dynamic_frame.from_options("s3", {"paths": [
                                                            f"s3://json-file-repo/test.json"]}, format="json", transformation_ctx="datasource0")
df = datasource0.toDF()
df = df.select(explode_outer('clients').alias("clients"))
list = [x["clients"] for x in df.rdd.collect()]
for client in list:
    bucket_name = client
    bucket = s3.Bucket(bucket_name)
    print(bucket_name)
    # for obj in bucket.objects.all() :
    # if obj.key.endswith('.csv') :
    datasource0 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": '"', "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={
                                                                "paths": [f"s3://{bucket_name}/"], "recurse": True, }, transformation_ctx="datasource0")
    # datasource0.printSchema()
    datasource0.toDF().show()
    print('\n\n\n\n\n\n')
