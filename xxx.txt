
##############################
REMEMBER to activate the virtual environment
Windows
.\Scripts\activate

Mac
source bin/activate

##############################
RUN THE SERVER
Windows
python -m bottle --server paste --bind 127.0.0.1:80 --debug --reload app

Mac
sudo python3 -m bottle --server paste --bind 127.0.0.1:80 --debug --reload app

##############################
STOP THE SERVER 
ctl+c many times, at least 2


##############################
RUN TAILWINDCSS
npx tailwindcss -i input.css -o ../app.css --watch


##############################
ROUTES/ROUTING

Create
Read
Update
Delete

/items                          GET - To get many items
/items/1                        GET - To get one item
/items                          POST - Create or save an item
/items/1                        DELETE - To delete an item
/items/1                        PUT or PATCH - To update the item









