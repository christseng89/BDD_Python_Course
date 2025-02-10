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