# Instagram_api
Here we'll be experimenting with the instagram API

# First we install the dependencies needed for this
sudo apt install python3-pip -y <br>
pip install instagrapi<br> 
sudo apt install postgresql postgresql-contrib -y<br>
sudo systemctl start postgresql.service<br>
sudo apt install postgresql-server-dev-XX -y #should be the same version<br>


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

{'pk': '39184300450', 'username': 'adr.bck', 'full_name': 'Adrian P̩̭̺̝͖̯̔̌ͦ̋̊̍̆', 'is_private': False, 'profile_pic_url': HttpUrl('https://instagram.fasu10-1.fna.fbcdn.net/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT8VM4mVHpV0cU1FUbunDBFLAE8cEM11_Bna3DwTiGNOmA&oe=631D9067&_nc_sid=7bff83', scheme='https', host='instagram.fasu10-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg', query='stp=dst-jpg_s150x150&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT8VM4mVHpV0cU1FUbunDBFLAE8cEM11_Bna3DwTiGNOmA&oe=631D9067&_nc_sid=7bff83'), 'profile_pic_url_hd': HttpUrl('https://instagram.fasu10-1.fna.fbcdn.net/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT8DdgTQnmS7BLrQ65Ugs8rqOJ-s1SUHyO2lvUbxOJ4Gsw&oe=631D9067&_nc_sid=7bff83', scheme='https', host='instagram.fasu10-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg', query='stp=dst-jpg_s320x320&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT8DdgTQnmS7BLrQ65Ugs8rqOJ-s1SUHyO2lvUbxOJ4Gsw&oe=631D9067&_nc_sid=7bff83'), 'is_verified': False, 'media_count': 36, 'follower_count': 48, 'following_count': 77, 'biography': '𝕊𝕖𝕥 𝕪𝕠𝕦𝕣 𝕙𝕖𝕒𝕣𝕥 𝕒𝕓𝕝𝕒𝕫𝕖 🔥\n𝕄𝕒𝕟𝕜𝕚𝕟𝕕 𝕨𝕒𝕤 𝕓𝕠𝕣𝕟 𝕠𝕟 𝕖𝕒𝕣𝕥𝕙 𝕓𝕦𝕥 𝕟𝕖𝕧𝕖𝕣 𝕞𝕖𝕒𝕟𝕥 𝕥𝕠 𝕕𝕚𝕖 𝕙𝕖𝕣𝕖🚀🪐\nℂ𝕠𝕞𝕡𝕦𝕥𝕖𝕣 𝕊𝕔𝕚𝕖𝕟𝕔𝕖 ⚡\n𝕌ℙ𝕋ℙ - ℕ𝕋𝕌𝕊𝕋', 'external_url': None, 'account_type': None, 'is_business': False, 'public_email': None, 'contact_phone_number': None, 'public_phone_country_code': None, 'public_phone_number': None, 'business_contact_method': 'UNKNOWN', 'business_category_name': None, 'category_name': 'Gamer', 'category': None, 'address_street': None, 'city_id': None, 'city_name': None, 'latitude': None, 'longitude': None, 'zip': None, 'instagram_location_id': None, 'interop_messaging_user_fbid': None}<br>





