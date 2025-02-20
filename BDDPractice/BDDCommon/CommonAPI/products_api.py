
from BDDCommon.CommonHelpers.wooRequestHelpers import WooRequestsHelper
from BDDCommon.CommonConfigs.configurations import get_config
import pdb


def list_all_products():
    """
    Retrieves all WooCommerce products without the 100,000 records limitation.
    """

    all_products = []
    page_num = 1  # Start from page 1
    per_page = int(get_config()['mysql']['per_page']) # Get the number of records per page

    while True:
        params = {'per_page': per_page, 'page': page_num}

        # Fetch response and headers
        woo_helper = WooRequestsHelper()
        rs_api = woo_helper.get(wc_endpoint='products', params=params)

        print(f"Fetching Page: {page_num}")

        if rs_api:
            all_products.extend(rs_api)

            # Check if we've reached the last page using WooCommerce API headers
            total_pages = int(woo_helper.rs.headers.get('X-WP-TotalPages', page_num))
            if page_num >= total_pages:
                print(f"✅ Retrieved all {total_pages} pages. Total products: {len(all_products)}")
                break

            page_num += 1  # Move to the next page
        else:
            print(f"❌ No results found on page {page_num}. Ending retrieval.")
            break

    return all_products

def get_product_by_id(product_id):
    """

    """

    rs_api = WooRequestsHelper().get(wc_endpoint="products/{}".format(product_id))

    return rs_api