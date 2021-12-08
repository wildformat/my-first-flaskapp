
cd sampe_flask
echo "===== build new application image ====="
docker build -t sample_flask:v1 .

echo "===== run built app image with exposed port forwarded locally while providing an interactive shell ====="
docker run --name sample-app -it --rm -p 127.0.0.1:5005:5000 sample_flask:v1