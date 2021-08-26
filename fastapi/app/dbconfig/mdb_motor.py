import motor.motor_asyncio

client = motor.motor.asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.