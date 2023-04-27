# asynchronous-api-calls-python-with-aws-lambda-function
With Aws lambda function - API - S3 Bucket this simple asynchronous python program is created

steps to implement:
1. Need Aws account and these three services (lambda - api - s3)
2. After enabling these sevices use lambda function to save/deploy this code - #post api function.py
3. Create an API gatway for this #post api function.py lambda function and get the endpoint url/request body
4. Copy of the url endpoint and past it in notepad file, like I did in this file - #post function url.txt
5. upload the #post function url.txt into S3 Bucket
6. Next create another lambda function named #async boto api call.py which will call the .txt file from S3 bucket and return the response of the previews lambda function(#post api function.py)

