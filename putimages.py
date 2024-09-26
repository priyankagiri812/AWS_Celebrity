
import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('Image1.jfif','Priyanka Chopra'),
('Image2.jfif','Alia Bhatt'),
('Image3.jfif','Katrina Kaif'),
('Image4.jfif','ShahRukh Khan'),
('Image5.jfif','Vicky Kaushal'),
('Image6.jfif','Kareena Kapoor'),
('Image7.jfif','Aishwarya Rai'),
('Image8.jfif','Hritik Roshan'),
('Image9.jfif','Ram Charan'),
('Image10.jfif','Shahid Kapoor'),
('Image11.jfif','Ranbir Kapoor'),
('Image12.jfif','Mahesh Babu'),
('Image13.jfif','John Ibrahim'),
('Image14.jfif','Allu Arjun'),
('Image15.jfif','Saif Ali Khan'),
('Image16.jfif','Karthick Aryan'),
('Image17.jfif','Shubhman Gill'),
('Image18.jfif','Mahendra Singh Dhoni'),
('Image19.jfif','Rohit sharma'),
('Image20.jfif','Shreyas Ayyar'),
('Image21.jfif','Virat Kohli')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('mybucketforcelebrities','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})