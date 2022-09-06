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

values: impressions, reach, follower_count, email_contacts, phone_call_clicks, text_message_clicks, get_directions_clicks, website_clicks, profile_views, audience_gender_age, audience_locale, audience_country, audience_city, online_followers, accounts_engaged, total_interactions, likes, comments, shares, saves, replies, engaged_audience_demographics, reached_audience_demographics, follower_demographics, follows_and_unfollows, profile_links_taps"

period[0] must be one of the following values: day, week, days_28, month, lifetime"
metric_type must be one of the following values: default, time_series, total_value"


