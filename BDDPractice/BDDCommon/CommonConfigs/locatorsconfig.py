

LOCATORS = {
    'main navigation' : {'type': 'id', 'locator':'mainnav'},
    'top navigation' : {'type': 'id', 'locator':'top'},
    'options' : {'type': 'css selector', 'locator':'.options-bar'}
}

MY_ACCOUNT_LOCATORS = {
    'login_user_name' : {'type': 'id', 'locator': 'username'},
    'login_user_password' : {'type': 'id', 'locator': 'password'},
    'login_btn' : {'type': 'css selector', 'locator': 'button[name="login"]'},
    'left_nav' : {'type': 'css selector', 'locator': 'div.entry-content nav.woocommerce-MyAccount-navigation'},
    'left_nav_logout_btn' : {'type': 'css selector', 'locator': 'div.entry-content nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)'},
    'error_box' : {'type': 'css selector', 'locator': 'ul.woocommerce-error'},

}

HOME_PAGE_LOCATORS = {
    'all_add_cart_btns': {'type': 'css selector', 'locator': 'li.product a.ajax_add_to_cart'},
    'cart_info_box': {'type': 'css selector', 'locator': 'ul.site-header-cart'},

}

CART_PAGE_LOCATORS = {
    'free_shipping_radio': {'type': 'css selector', 'locator': 'li input#shipping_method_0_free_shipping5'},
    # FIX: Updated the correct selector for 'Proceed to Checkout'
    'proceed_to_checkout_btn': {'type': 'css selector', 'locator': 'a.wc-block-components-button.wp-element-button.wc-block-cart__submit-button.contained'},
    'total_cart_value': {'type': 'css selector', 'locator': 'div.wc-block-components-totals-item__value span.wc-block-formatted-money-amount'},
    'add_a_coupon_button': {'type': 'css selector', 'locator': 'div.wc-block-components-panel__button'},
    # 'coupon_code_field': {'type': 'css selector', 'locator': 'input#wc-block-components-totals-coupon__input'},
    'coupon_code_field': {'type': 'css selector', 'locator': 'input#wc-block-components-totals-coupon__input-coupon'},
    'apply_coupon_button': {'type': 'css selector', 'locator': 'button.wc-block-components-totals-coupon__button'}
}

CHECKOUT_PAGE_LOCATORS = {
    'page_header': {'type': 'css selector', 'locator': 'h1.entry-title'},
    'checkout_form': {'type': 'css selector', 'locator': 'form.wc-block-components-form.wc-block-checkout__form'}, # Updated locator
    'billing_email_input': {'type': 'css selector', 'locator': 'input#email'},
    'billing_f_name_input': {'type': 'css selector',
                             'locator': 'input#billing_first_name, input[name="billing_first_name"], input[autocomplete="given-name"]'},
    'billing_l_name_input': {'type': 'css selector',
                             'locator': 'input#billing_last_name, input[name="billing_last_name"], input[autocomplete="family-name"]'},
    'billing_company_input': {'type': 'css selector', 'locator': 'input#billing_company'},
    'billing_address1_input': {'type': 'css selector',
                               'locator': 'input#billing-address_1, input[autocomplete="address-line1"]'},
    'billing_city_input': {'type': 'css selector',
                           'locator': 'input#billing-city, input[autocomplete="address-level2"]'},
    'billing_state_input': {'type': 'css selector',
                            'locator': 'input#billing-state, input[autocomplete="address-level1"]'},
    'billing_zip_input': {'type': 'css selector', 'locator': 'input#billing-postcode, input[autocomplete="postal-code"]'},

    'billing_phone_input': {'type': 'css selector', 'locator': 'input#billing-phone, input[autocomplete="tel"]'},
    'place_order_btn': {'type': 'css selector', 'locator': 'button.wc-block-components-button.wp-element-button.wc-block-components-checkout-place-order-button.contained'}
}


ORDER_RECEIVED_LOCATORS = {
    'page_header': {'type': 'css selector', 'locator': 'header.entry-header h1.entry-title'},
    'thankyou_notice': {'type': 'css selector', 'locator': 'div.woocommerce-order p.woocommerce-thankyou-order-received'},
    'order_details_order': {'type': 'css selector', 'locator': 'ul.order_details li.order'},
    'order_details_date': {'type': 'css selector', 'locator': 'ul.order_details li.date'},
    'order_details_total': {'type': 'css selector', 'locator': 'ul.order_details li.total'},
    'order_details_method': {'type': 'css selector', 'locator': 'ul.order_details li.method'},

}





