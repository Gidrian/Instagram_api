# Instagram_api
Here we'll be experimenting with the instagram API

# First we install the dependencies needed for this
sudo apt install python3-pip -y
pip install instagrapi 
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql.service
sudo apt install postgresql-server-dev-XX -y #should be the same version
sudo apt-get install -y liburiparser-dev
sudo apt-get install git -y
git clone https://github.com/petere/pguri.git
make
sudo make install


pip install psycopg2



postgres database commands:
CREATE EXTENSION uri;
CREATE TABLE InstagramUser (
	user_id serial UNIQUE PRIMARY KEY,
	username TEXT  UNIQUE NOT NULL,
	full_name TEXT,
	is_private BOOLEAN NOT NULL,
	profile_pic_url TEXT,
	profile_pic_url_hd TEXT,
	is_verified BOOLEAN DEFAULT FALSE,
	media_count NUMERIC,
	follower_count NUMERIC,
	following_count NUMERIC,
	biography TEXT,
	external_url TEXT,
	account_type TEXT,
	is_business BOOLEAN DEFAULT FALSE,
	public_email TEXT,
	contact_phone_number TEXT,
	public_phone_country_code TEXT,
	public_phone_number TEXT,
	business_contact_method TEXT,
	business_category_name TEXT,
	category_name TEXT,
	address_street TEXT,
	city_id NUMERIC,
	city_name TEXT,
	latitude TEXT,
	longitude TEXT,
	instagram_location_id NUMERIC
);

'account_type': None, 'is_business': False, 'public_email': None, 'contact_phone_number': None, 'public_phone_country_code': None, 'public_phone_number': None, 'business_contact_method': 'UNKNOWN', 'business_category_name': None, 'category_name': 'Gamer', 'category': None, 'address_street': None, 'city_id': None, 'city_name': None, 'latitude': None, 'longitude': None, 'zip': None, 'instagram_location_id': None, 'interop_messaging_user_fbid': None}





