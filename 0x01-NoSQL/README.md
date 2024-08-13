What is NoSQL?
NoSQL stands for "Not Only SQL." It refers to a broad category of database management systems that are designed to handle large volumes of unstructured or semi-structured data, offering flexible data models that do not require a fixed schema like traditional relational databases (SQL). NoSQL databases are optimized for specific use cases, such as handling large-scale distributed data, providing high availability, and enabling efficient horizontal scaling.

Difference Between SQL and NoSQL
Data Model:
SQL: Uses a structured, table-based model with predefined schemas, where data is organized into rows and columns.
NoSQL: Uses flexible data models such as key-value pairs, documents, wide-column stores, or graphs, which allow for more dynamic and unstructured data storage.

Scalability:
SQL: Generally scales vertically by adding more power (CPU, RAM) to a single server.
NoSQL: Typically scales horizontally by adding more servers, making it ideal for distributed systems.

Schema:
SQL: Requires a predefined schema, meaning the structure of data must be known in advance.
NoSQL: Does not require a fixed schema, allowing for the storage of various data types in the same collection.

ACID Compliance:
SQL: Fully supports ACID properties (Atomicity, Consistency, Isolation, Durability), ensuring reliable transactions.
NoSQL: May not fully support ACID properties, as they are often relaxed to achieve better performance and scalability.

Use Cases:
SQL: Ideal for complex queries, structured data, and applications requiring strict consistency.
NoSQL: Best suited for large-scale data storage, real-time web applications, and use cases with varying data structures.

What is ACID?
ACID is an acronym representing a set of properties that ensure reliable database transactions:

Atomicity: Ensures that all operations within a transaction are completed successfully. If any operation fails, the entire transaction is rolled back.
Consistency: Guarantees that a transaction takes the database from one valid state to another, maintaining data integrity.
Isolation: Ensures that concurrent transactions do not interfere with each other. Each transaction is executed as if it were the only one in the system.
Durability: Once a transaction is committed, it is permanently recorded in the database, even in the event of a system failure.
What is Document Storage?
Document storage is a type of NoSQL database where data is stored in documents, typically using a format like JSON or BSON (Binary JSON). Each document can contain a wide variety of data, including nested documents, arrays, and key-value pairs. Document stores offer a flexible schema, allowing different documents within the same collection to have different structures.

Types of NoSQL Databases
Document Stores: Store data in document format (e.g., MongoDB, CouchDB).
Key-Value Stores: Use a simple key-value pair model (e.g., Redis, DynamoDB).
Column-Family Stores: Store data in columns instead of rows, often used for large-scale distributed data (e.g., Cassandra, HBase).
Graph Databases: Store data as nodes, edges, and properties, ideal for handling relationships (e.g., Neo4j, OrientDB).

Benefits of NoSQL Databases
Flexibility: Can store unstructured and semi-structured data without a fixed schema.
Scalability: Easily scales horizontally by adding more servers, making it suitable for distributed systems.
Performance: Optimized for fast reads and writes, especially with large datasets.
High Availability: Often designed with built-in replication and distribution features to ensure data availability.
Big Data: Capable of handling large volumes of data, making it ideal for big data applications.

Querying Information from a NoSQL Database
The way to query data depends on the type of NoSQL database:

Using MongoDB
Setting Up MongoDB
Install MongoDB:
Follow the installation instructions for your operating system from the MongoDB website.

Start MongoDB:
Start the MongoDB service:
mongod

Access the MongoDB Shell:
mongo

Basic MongoDB Operations

Create a Database:
use mydatabase;

Create a Collection:
db.createCollection("mycollection");

Insert a Document:
db.mycollection.insertOne({ "name": "John Doe", "age": 30 });

Query Documents:
db.mycollection.find({ "age": { $gt: 25 } });

Update a Document:
db.mycollection.updateOne({ "name": "John Doe" }, { $set: { "age": 31 } });

Delete a Document:
db.mycollection.deleteOne({ "name": "John Doe" });
Shut Down MongoDB:

To shut down the MongoDB server, you can use the following command in the MongoDB shell:
use admin;
db.shutdownServer();

MongoDB in a Node.js Application
Install MongoDB Driver:
npm install mongodb

Connect to MongoDB:
const { MongoClient } = require('mongodb');
const uri = "mongodb+srv://username:password@cluster0.mongodb.net/mydatabase";
const client = new MongoClient(uri);

async function run() {
    try {
        await client.connect();
        console.log("Connected to MongoDB");
    } finally {
        await client.close();
    }
}

run().catch(console.dir);
Perform CRUD Operations:
Use the MongoDB driver methods like insertOne, find, updateOne, and deleteOne to interact with your MongoDB collections.

