#!/bin/bash
echo "Beginning() to install apache" >> /tmp/log.txt
sudo yum update
sudo yum install httpd -y
sudo systemctl enable httpd
sudo service httpd start
sudo yum install python3

echo "<h2>Test page</h2> Instance ID: " >> /var/www/html/index.html
curl --silent http://169.254.169.254/latest/meta-data/instance-id/ >> /var/www/html/index.html
echo "<br>Availability zone:" >> /var/www/html/index.html
curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/ >> /var/www/html/index.html
echo "<br>IP address: </td>" >> /var/www/html/index.html
curl --silent http://169.254.169.254/latest/meta-data/public-ipv4 >> /var/www/html/index.html
echo "<hr>Here is an image that I have stored on S3: <br>" >> /var/www/html/index.html
echo "<img src=https://s3-eu-west-1.amazonaws.com/%s/embed2.jpg>" >> /var/www/html/index.html
echo "Apache was installed" >> /tmp/log.txt