# Instagram_api
Here we'll be experimenting with the instagram API

# First we install the dependencies needed for this
sudo apt install python3-pip -y <br>
pip install instagrapi<br> 
sudo apt install postgresql postgresql-contrib -y<br>
sudo systemctl start postgresql.service<br>
sudo apt install postgresql-server-dev-XX -y #should be the same version<br>
make<br>
sudo make install<br>


(not yet) pip install psycopg2<br>



postgres database commands:<br>
CREATE EXTENSION uri;<br>
CREATE TABLE InstagramUser (<br>
	user_id serial UNIQUE PRIMARY KEY,<br>
	username TEXT  UNIQUE NOT NULL,<br>
	full_name TEXT,<br>
	is_private BOOLEAN NOT NULL,<br>
	profile_pic_url TEXT,<br>
	profile_pic_url_hd TEXT,<br>
	is_verified BOOLEAN DEFAULT FALSE,<br>
	media_count NUMERIC,<br>
	follower_count NUMERIC,<br>
	following_count NUMERIC,<br>
	biography TEXT,<br>
	external_url TEXT,<br>
	account_type TEXT,<br>
	is_business BOOLEAN DEFAULT FALSE,<br>
	public_email TEXT,<br>
	contact_phone_number TEXT,<br>
	public_phone_country_code TEXT,<br>
	public_phone_number TEXT,<br>
	business_contact_method TEXT,<br>
	business_category_name TEXT,<br>
	category_name TEXT,<br>
	address_street TEXT,<br>
	city_id NUMERIC,<br>
	city_name TEXT,<br>
	latitude TEXT,<br>
	longitude TEXT,<br>
	instagram_location_id NUMERIC<br>
);<br>

'account_type': None, 'is_business': False, 'public_email': None, 'contact_phone_number': None, 'public_phone_country_code': None, 'public_phone_number': None, 'business_contact_method': 'UNKNOWN', 'business_category_name': None, 'category_name': 'Gamer', 'category': None, 'address_street': None, 'city_id': None, 'city_name': None, 'latitude': None, 'longitude': None, 'zip': None, 'instagram_location_id': None, 'interop_messaging_user_fbid': None}<br>





