import subprocess
import os

def install_botocore_boto3():
  """Installs botocore and boto3 libraries using pip."""
  try:
    subprocess.run(['pip', 'install', 'botocore', 'boto3'], check=True)
    print("Successfully installed botocore and boto3 libraries.")
  except subprocess.CalledProcessError as e:
    print(f"Error installing libraries: {e}")

# Install botocore and boto3 before running the playbook
install_botocore_boto3()

slack_token = os.getenv('SLACK_TOKEN')
aws_access_key = os.getenv('ACCESS_KEY')
aws_secret_key = os.getenv('SECRET_KEY')
aws_region = os.getenv('REGION')
ssh_port = os.getenv('SSH_PORT')
private_key = os.getenv('PRIVATE_KEY')

extra_vars = f"slack_token={slack_token} aws_access_key={aws_access_key} aws_secret_key={aws_secret_key} aws_region={aws_region} ssh_port={ssh_port} private_key={private_key}"

result = subprocess.run(['ansible-playbook', 'playbook-one.yml' , '--extra-vars', extra_vars])
if result.returncode == 0:
  print("Playbook 1 successful")
else:
  print("Playbook 1 failed")
  subprocess.run(['ansible-playbook', 'playbook-two.yml', '--extra-vars', extra_vars])