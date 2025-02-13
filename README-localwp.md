# Local WordPress

## Download LocalWP
https://localwp.com/ => Download LocalWP

### Install LocalWP
- Program Folder
    - C:\Program Files (x86)\LocalWP

- WebServer
    - nginx
- WordPress Admin
    - Username: admin
    - Password: admin$123
- MySQL Admin
    - Username: root
    - Password: root$123

### Create a new site
- ❌ -> Create new user/Reports
- ➕ -> Create a new site => Continue
    - Site Name: mylocalwp => Continue
    - Preferred => Continue
    - WordPress Admin
        - Username: admin
        - Password: admin$123 => Add Site

- WP Admin => Browser (http://mylocalwp.local/wp-admin/)
    - Username: admin
    - Password: admin$123

- Open Site => Browser (http://mylocalwp.local/)

### Install Theme
- WP Admin => Appearance => Themes => Add New Theme
    - Search: storefront
    - Install => Activate
- Open Site => Browser (http://mylocalwp.local/)

### Install Plugin
- WP Admin => Plugins => Add New Plugin
    - Search: woocommerce
    - Install Now => Activate

- WooCommerce => Settings => General
    - Store Address
        - Country / Region: China
    - Currency Options
        - Currency: US Dollars ($)
    - Save changes

### Adding sample products
https://woocommerce.com/document/importing-woocommerce-sample-data/ => Re-download WooCommerce

- Tools -> Import -> WordPress -> Install Now -> Run Importer -> 
  Choose File -> WooCommerce Sample Data -> Upload file and import
  (sample_products.csv, sample_products.xml)
    - Shop Manager: admin
    - 'v' Download and import file attachment
    - Submit

### Setup Home Page and Registration
- Settings -> Reading
    - Your homepage displays: A static page (select below)
        - Homepage: Shop
    - Save changes

- Settings -> General
    - Membership
        - Anyone can register
    - Save changes
  
- WooCommerce -> Settings -> Accounts & Privacy
    - Checkout
        - Enable login during checkout
    - Account creation
        - During checkout
        - Allow customers to create an account on the "My account" page
    - Save changes

### Use 'Coupons' to checkout
- WooCommerce -> Coupons
    - Add Coupon
        - Coupon code: 10off
        - Description: 10% off
        - Discount type: Percentage discount
        - Coupon amount: 10
        - Allow free shipping: ✅
        - Coupon expiry date (optional): 2025-02-28
        - Usage restriction
            - Minimum spend: 20
            - Individual use only: ✅
        - Usage limits
            - Usage limit per coupon: 1
        - Publish
      
### Checkout with "Cash on Delivery"
- WooCommerce -> Settings -> Payments
    - Cash on delivery
        - Enable: ✅

- WooCommerce -> Settings -> Orders
    - Order -> Status (Completed) -> Update

### Setup and Test WooCommerce Rest API
https://woocommerce.com/document/woocommerce-rest-api/
- WooCommerce -> Settings -> Advanced -> REST API
    - Add key
        - Description: Test
        - User: admin
        - Permissions: Read/Write -> Generate API key

Customer Key: ck_b05a8107856c44b688ae9f6263a549dccc84af16
Secret Key: cs_718fb79852941b5cfe7288788296626c3a6558ae

https://woocommerce.github.io/woocommerce-rest-api-docs/#introduction

Test by Postman / Python / etc.

### Connecting to Database
- LocalWP -> Database -> OpenAdminerEvo
    - Server: localhost
- MySQL Workbench
    - Connection Name: LocalWP
    - Connection Method: Standard (TCP/IP)
    - Port: 10005
    - Username: root
    - Password: root

SELECT * FROM local.wp_wc_orders;

https://github.com/woocommerce/woocommerce/wiki/Database-Description

### Docker Swarm
https://github.com/dhinojosac/localwp2docker-wordpress

### WP SMTP Plugin

1. Install WP Mail SMTP
    Plugins => Search (WP Mail SMTP by WPForms) => Install Now => Activate
2. Generate a Gmail App Password
    Go to Google App Passwords
    Select Mail as the app
    Choose Other (Custom Name) and enter "LocalWP SMTP"
    Copy the generated password (you’ll use this instead of your Gmail password)

3. Configure WP Mail SMTP (Free Version)

    Go to WP Mail SMTP → Settings
    Choose Other SMTP as the mailer
    Enter these settings:

        SMTP Host: smtp.gmail.com
        SMTP Port: 587
        Encryption: TLS
        Authentication: Yes
        Username: your_email@gmail.com
        Password: [Your App Password from Step 1]
        Save changes and send a test email

4. WooCommerce -> Settings -> Site visibility -> Live -> Save changes

5. Plugins -> Add New -> Upload Plugin -> 
    - Choose File: wp-smtp.zip
    - Install Now
    - Activate Plugin

### Backup and Restore
Install plugin -> Migration, Backup, Staging – WPvivid Backup & Migration -> Activate -> Backup Now
