import boto3
import boto3.session
from util import AESCipher

session = boto3.session.Session(region_name='eu-west-1')
s3Client = session.client('s3')


data = open('manage.py', 'rb')
cipher = AESCipher(key='1234567890123456')
encrypted = cipher.encrypt(data.read().decode('utf-8'))
print(encrypted)
s3Client.put_object(Bucket='reciproco',Key='manage.py', Body=encrypted)


print(s3Client.generate_presigned_url('get_object', Params = {'Bucket': 'reciproco', 'Key': 'manage.py'}, ExpiresIn = 100))

new_cipher = AESCipher(key='1234567890123456')
response = s3Client.get_object(Bucket='reciproco',Key='manage.py')
i = response["Body"].read()
print(i)
decrypted = new_cipher.decrypt(i)
print(decrypted.decode('utf-8'))
