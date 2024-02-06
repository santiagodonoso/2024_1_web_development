REMEMBER to activate the virtual environment

Windows
python -m bottle --server paste --bind 127.0.0.1:80 --debug --reload app

Mac
sudo python3 -m bottle --server paste --bind 127.0.0.1:80 --debug --reload app

Stop the server 
ctl+c many times, at least 2


Run tailwindcss
npx tailwindcss -i input.css -o ../app.css --watch
