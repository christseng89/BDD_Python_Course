Feature:  “create user” and “create coupon” API call

    Scenario Outline:  make “<call>” with “<data>” data

        Given make “<call>” API call with “<data>” data
        Then the response should have “<status code>” status code and “<message>” message

        Examples:
            |     call      | data  | status code | message |
            |  create user  | good  |     200     | success |
            |  create user  | bad   |     500     |  error  |
            | create coupon | good  |     200     | success |
            | create coupon | bad   |     500     |  error  |
