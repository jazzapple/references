/* ******************************************** */
/*	AWS Big Data Training 						*/
/*	05/09/2018									*/
/* ******************************************** */

/* Resources */
https://aws.amazon.com/new/
https://calculator.s3.amazonaws.com/index.html
https://aws.amazon.com/blogs/big-data/analyzing-data-in-s3-using-amazon-athena/
https://registry.opendata.aws/
https://reinvent.awsevents.com/learn/sessions/
https://aws.amazon.com/free/

/* ******************* 	*/
/* Big Data Pipeline 	*/
/* ******************* 	*/
Services for collecting and moving it: 
- Kinesis Firehose (real time stream)
- Snowball (batch import/export)
- SQS (messsage queuing)
- EC2 (web/app servers)

Services for storing it:
- S3, Glacier (archival - hrs latency for retrieval) - object storage
- DynamoDB (NoSQL) - use for storing metadata. Cannot join tables natively - need to extract/read via spark cluster first. The optimal use cases for DynamoDB require a durable data store for high-velocity data. Applications such as online voting and registration, gaming, and digital advertising are all popular use cases for DynamoDB.

Process and analyse
- EMR - dynamic load and allocation resource manager. You should use Amazon EMR if you use custom code to process and analyze extremely large datasets with big data processing frameworks such as Apache Spark, Hadoop, Presto, or Hbase. Amazon EMR gives you full control over the configuration of your clusters and the software you install on them.
- Lambda, Kinesis Analytics - near real-time. Kinesis Analytics is not available in Australia yet. Fraud use cases - stores queries and runs against streamed data
- Redshift - denormalised database, distributed processing
- SageMaker - machine learning
- Athena - managed Presto/Hive service - ad hoc analytics

/* ******************* 	*/
/* Data Ingestion 		*/
/* ******************* 	*/
Transactional
Transactional data must be able to quickly store and retrieve small pieces of data. End users need quick and straightforward access to the data, which makes app and web servers the ideal ingestion methods. For the same reasons, databases, such as DynamoDB and Amazon RDS, are usually the best solution for these kinds of processes.

File
Data transmitted through individual files typically is ingested from connected devices. This kind of log data does not require fast storage and retrieval like transactional data does, and also transfer is one-way, so ingestion can come from a wide-variety of sources. This kind of data is typically stored in Amazon S3.

Stream
Stream data, such as click-stream logs, should be ingested through an appropriate solution such as an Amazon Kinesis-enabled application or Fluentd. Initially, these logs are stored in stream storage solutions such as Amazon Kinesis, so theyre available for real-time processing and analysis. Long-term storage of these logs is best in a low-cost solution such as Amazon S3. "pushes" the data past the query. Kinesis Stream is unmanaged. Firehose is the managed service. 
Amazon Kinesis Data Firehose is the easiest way to load streaming data into AWS. It can capture, transform, and load streaming data into Amazon Kinesis Data Analytics, Amazon S3, Amazon Redshift, and Amazon Elasticsearch Service, enabling near real-time analytics. Scales automatically, but longer processing latency. 

Transferring data into S3 
- multipart ideal for files >100MB
- AWS Snowball is a petabyte-scale (physical) data transport solution that uses secure appliances to transfer large amounts of data into and out of AWS.

/* ***************************	*/
/* Streaming data with Kinesis 	*/
/* *************************** 	*/
Streaming Analytics
- Supports SQL queries on incoming streat data BEFORE it is stored or processed
- Use cases - real time alerts and initiate responses

Shards are storage mechanisms for streams within Kinesis Stream. 

/* ******************* 	*/
/* Storage 				*/
/* ******************* 	*/
S3 
- unless you move data out of the region, retreival cost (put/list requests) is minimal
- free to create a bucket. Charges apply once data is stored in buckets

NoSQL databases
- require partition and sort keys. Cannot query efficiently along keys that are not sort keys

Redshift
Amazon Redshift delivers fast query performance by using columnar storage technology to improve I/O efficiency and parallelizing queries across multiple nodes.
Redshift uses standard PostgreSQL JDBC and ODBC drivers, allowing you to use a wide range of familiar SQL clients. Data load speed scales linearly with cluster size, with integrations to Amazon S3, DynamoDB, Amazon EMR, Amazon Kinesis, or any SSH-enabled host. Amazon Redshift automates most of the common administrative tasks associated with provisioning, configuring, and monitoring a data warehouse. Backups to Amazon S3 are continuous, incremental and automatic. Restores are fast; you can start querying in minutes while your data is spooled down in the background.

RDS (Relational Database Service)
A managed web service that makes it easy to set up, operate, and scale a relational database in the cloud. Amazon RDS gives you access to the capabilities of a familiar MySQL, Oracle, Microsoft SQL Server, or PostgreSQL database engine. This means that the code, applications, and tools you already use today with your existing databases can be used with Amazon RDS. You benefit from the flexibility of being able to scale the compute resources or storage capacity associated with your database instance via a single API call.
Apache Sqoop is an open source software package that allows you to transfer data between Hadoop and a relational database. Sqoop supports bi-directional transfer; it can be used to import data from a relational database into HDFS and to export data from HDFS into a relational database. The data is imported and exported using MapReduce and can be transformed before it is exported.

When would I use Amazon Redshift vs. Amazon RDS?
Both Amazon Redshift and Amazon RDS enable you to run traditional relational databases in the cloud while offloading database administration. Customers use Amazon RDS databases both for online-transaction processing (OLTP) and for reporting and analysis. Amazon Redshift harnesses the scale and resources of multiple nodes and uses a variety of optimizations to provide order of magnitude improvements over traditional databases for analytic and reporting workloads against very large data sets. Amazon Redshift provides an excellent scale-out option as your data and query complexity grows or if you want to prevent your reporting and analytic processing from interfering with the performance of your OLTP workload.

/* ******************* 	*/
/* Processing 			*/
/* ******************* 	*/
Amazon Athena - ad hoc analysis
An interactive query managed service that makes it easy to analyze data in Amazon S3 and DynamoDB using standard SQL. Athena is serverless, so there is no infrastructure to setup or manage, and you can start analyzing data immediately. Hive describes the data (schema on read), Presto processes (SQL)
You can query your data directly from Amazon S3 without having to move data to a Hadoop cluster or a data warehouse. You do not need to perform any ETL on the data. Query performance improves if you convert your data to open source columnar formats such as Apache Parquet or ORC.
The cost of Athena is based on the number of bytes scanned . No charges for DDL statements (CREATE/ALTER/DROP TABLE) statements for managing partitions, or failed queries. Cancelled query costs are based on amount of data scanned. 

/* ******************* 	*/
/* EMR 					*/
/* ******************* 	*/
Amazon EMR is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts of data. 
Your EMR cluster consists of EC2 (Amazon Elastic Compute Cloud) instances, which perform the work that you submit to your cluster. 
Enables decoupling of storage (S3) and compute (EMR)

Cluster comprised of Nodes: 
- Master - manages the cluster by running software components to coordinate the distribution of data and tasks among other nodes for processing. The master node tracks the status of tasks and monitors the health of the cluster. Every cluster has a master node, and it is possible to create a single-node cluster with only the master node.
- Core - contains software components that run tasks and store data in the Hadoop Distributed File System (HDFS) on your cluster. Multi-node clusters have at least one core node.
- Task - contains software components that only runs tasks and does not store data in HDFS. Task nodes are optional.

Options for building a cluster: 
1. quickstart GUI
2. AMI files
3. Teraform / command line script

S3 can be used with EMR in one of two ways: as an input/output repository for EMR (with HDFS used for the MapReduce processing phase) or as a replacement for HDFS. Maintaining data in S3 allows you to persist it. 

/* *************************** 	*/
/* Hadoop Processing Frameworks */
/* *************************** 	*/
Hive
Language: HiveQL
Interpreter: Hive
Engine: MapReduce, Spark, Tez
Main use case: effectively join large tables

Presto
Language: SQL
Engine: Presto
Main use case: optimised query performance

Pig
Language: Pig Latin
Interpreter: Pig
Engine: MapReduce, Tez
Main use case: Tranforms (ETL). Not intended to be a query language

Spark
Language: Spark, Spark SQL, Scala, Java, Python
Engine: Spark
Main use case: enables data mining and querying big datasets at fast speeds

/* ******************* 	*/
/* Spark 				*/
/* ******************* 	*/
Spark operations perform transformations and actions. Transformations define new RDDs using operations such as map, filter, sample, groupByKey, reduceByKey, and sortByKey. Actions return a result using operations such as collect, reduce, count, save, and lookupKey.
By default, transformations are lazy operations. They form the RDDs only. An action executes the RDDs

Resilient distributed datasets (RDDs) are read-only distributed collections of objects that can be cached in memory across cluster nodes. They are manipulated through various parallel operators and are automatically rebuilt after failure (providing fault-tolerant distribution). RDDs can be re-used across operations and provide a way to manipulate and persist intermediate datasets.

Spark Libraries
- Spark 2.0 combines the DataFrame and Dataset API into one Dataset API. The entry point to Spark SQL is SparkSession from Spark 2.0. 
- Spark SQL: With Spark SQL, you can use SQL or the DataFrame API to query data. It is also usable in Java, Scala, Python, and R. In addition to being compatible with a variety of data sources, data can even be joined from multiple sources via Spark SQL
- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Supports Scala, Java, Python
- SparkML is the primary machine learning API as of Spark 2.0. It offers a scalable, distributed machine learning algorithm library—accessible via Sparks APIs—for use on top of Spark and all of Sparks other modules (Spark SQL, Spark Streaming, and GraphX). Supports Python, Java, Scala, SparkR
Types of machine learning algorithms included: 
	• Classification: logistic regression, linear support vector machine, naïve Bayes 
	• Regression: generalized linear regression (GLM) 
	• Collaborative filtering: alternating least squares (ALS) 
	• Clustering: k-means 
	• Decomposition: singular value decomposition (SVD), principal component analysis
- GraphX
- Hive: Alternative to running Hive on MapReduce or Tez

/* ******************* 	*/
/* Redshift 			*/
/* ******************* 	*/
Fast, powerful fully managed data warehouse service
Compute nodes are backed up and restored via S3 - so best to write any desired persistent data back to S3 rather than back to Redshift

Amazon Redshift Spectrum: efficiently query and retrieve structured and semi-structured data from files in Amazon S3 without having to load the data into Amazon Redshift tables. 

Amazon EMR is ideal for processing and transforming (ETL) unstructured or semi-structured data to bring in to Amazon Redshift and is also a much better option for data sets that are relatively transitory, not stored for long-term use. Amazon Redshift is ideal for large volumes of structured data that you want to persist and query using standard SQL and your existing BI tools.

Hive: If your business use case involves ad hoc SQL queries that do not require full-scale data warehousing functionality, Hive may be a better option. Although storage of large amounts of data in Amazon S3 is more expensive than using Amazon Redshift, you do have to manage loading data into Amazon Redshift, including any data manipulation required to properly structure the data.
Using Hive on Amazon EMR generates MapReduce code when queries are submitted.
This has a performance impact and makes complex SQL operations, such as complicated joins across several tables, more difficult.

Presto is similar to Hive; that is, it is a distributed SQL query engine, not a data warehouse solution. That makes it very different from Amazon Redshift in many ways. Primarily, although Amazon Redshift loads data into its clusters for fast querying and analysis, Presto runs queries against a separate storage solution.

/* ******************* 	*/
/* Security 			*/
/* ******************* 	*/
Key tennents
• Authentication (Key pairs: IAM - ldap + federation + SAML)
• Authorisation (IAM roles and policies)
• Accounting (Amazon Cloudwatch - metrics focussed)
• Audit (Amazon Cloudtrail)
• Encryption - at rest vs transit (Amazon Key Management Services, KMS)