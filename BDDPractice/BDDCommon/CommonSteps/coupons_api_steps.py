from behave import step
from BDDCommon.CommonHelpers.utilitiesHelpers import generate_random_coupon_code
from BDDCommon.CommonAPI import coupons_api
from BDDCommon.CommonDAO.couponsDAO import CouponsDAO
import json
# import sys


@step('I create a "{discount_type}" coupon')
def create_a_coupon_with_given_discount_type(context, discount_type):
    data = {
        "code": generate_random_coupon_code(),
    }
    if discount_type.lower() != 'none':
        context.expected_discount_type = discount_type
        data["discount_type"] = discount_type
    else:
        context.expected_discount_type = 'fixed_cart'

    try:
        rs_api = coupons_api.create_coupon(data)

        # Check that the API response is valid before accessing its keys
        if rs_api is None or 'id' not in rs_api or not rs_api['id']:
            raise Exception("Coupon API returned None. Please verify the API server and input parameters.")

    except Exception as e:
        raise Exception (f"❌ Exception Error: {e}")
        # sys.exit(1)

    context.new_coupon_info = rs_api
    coupon_id = context.new_coupon_info['id']
    print(f"✅ New coupon created: {data['code']}, id: {coupon_id}")


@step("the coupon should exist in database")
def the_coupon_should_exist_in_database(context):
    coupon_dao = CouponsDAO()
    coupon_id = context.new_coupon_info.get('id')
    if not coupon_id:
        raise Exception("❌ No coupon id found in context. Coupon creation may have failed.")

    db_coupon = coupon_dao.get_coupon_by_id(coupon_id)
    assert db_coupon, f'Coupon not found in database. Coupon id: {coupon_id}'

    coupon_meta = coupon_dao.get_coupon_metadata_by_id(coupon_id)
    assert coupon_meta['discount_type'] == context.expected_discount_type, (
        f"Unexpected 'discount_type' for new coupon. Expected: {context.expected_discount_type}, "
        f"Actual: {coupon_meta['discount_type']}"
    )

    print(f"✅ Coupon found in database. Coupon id: {coupon_id}")


@step("I create a coupon with given parameters")
def i_create_a_coupon_with_given_parameters(context):
    data_raw = context.text
    data = json.loads(data_raw)
    data['code'] = generate_random_coupon_code()

    try:
        rs_api = coupons_api.create_coupon(data)

        # Check that the API response is valid before accessing its keys
        if rs_api is None or 'id' not in rs_api or not rs_api['id']:
            raise Exception("Coupon API returned None. Please verify the API server and input parameters.")

    except Exception as e:
        raise Exception (f"❌ Exception Error: {e}")
        # sys.exit(1)

    context.new_coupon_info = rs_api
    coupon_id = context.new_coupon_info['id']
    print(f"✅ New coupon created: {data['code']}, id: {coupon_id}")


@step("I verify the given metadata in database")
def i_verify_the_given_metadata_in_database(context):
    expected_values_raw = context.text
    expected_values = json.loads(expected_values_raw)

    coupon_id = context.new_coupon_info.get('id')
    if not coupon_id:
        raise Exception("❌ No coupon id found in context. Coupon creation may have failed.")

    db_meta = CouponsDAO().get_coupon_metadata_by_id(coupon_id)
    failed_fields = []
    for key, value in expected_values.items():
        if str(db_meta.get(key)) != str(value):
            failed_fields.append({key: {'expected': value, 'db': db_meta.get(key)}})

    if failed_fields:
        raise Exception(f"❌ Metadata verification failed. Mismatched fields: {failed_fields}")

    print(f"✅ Coupon found in database. Coupon id: {coupon_id}")


@step("I get a valid {pct}% off coupon")
def i_get_a_valid_pct_coupon(context, pct):
    if int(pct) == 50:
        context.coupon_code = "TEST50"
    else:
        raise Exception("❌ Not implemented for the given percentage.")

    print(f"✅ Get a valid {pct}% coupon code: '{context.coupon_code}'")
