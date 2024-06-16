post_login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "user": {
      "type": "object",
      "properties": {
        "pk": {
          "type": "integer"
        },
        "username": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "first_name": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        },
        "role": {
          "type": "array",
          "items": [
            {
              "type": "string"
            }
          ]
        },
        "avatar": {
          "type": "null"
        },
        "vk": {
          "type": "boolean"
        },
        "facebook": {
          "type": "boolean"
        },
        "telegram": {
          "type": "boolean"
        },
        "email_subscribe": {
          "type": "boolean"
        },
        "telegram_subscribe": {
          "type": "boolean"
        },
        "vk_subscribe": {
          "type": "boolean"
        },
        "facebook_subscribe": {
          "type": "boolean"
        },
        "is_active": {
          "type": "boolean"
        },
        "is_blocked": {
          "type": "boolean"
        },
        "is_part_blocked": {
          "type": "boolean"
        },
        "favorites": {
          "type": "integer"
        },
        "reviews": {
          "type": "integer"
        },
        "my_serials": {
          "type": "integer"
        },
        "user_domain": {
          "type": "string"
        },
        "subscription": {
          "type": "null"
        },
        "user_subdomain": {
          "type": "string"
        },
        "quality_name": {
          "type": "string"
        },
        "quality_for_all": {
          "type": "boolean"
        },
        "phone": {
          "type": "null"
        },
        "has_obtained_films": {
          "type": "boolean"
        },
        "balance": {
          "type": "integer"
        },
        "referrer_link": {
          "type": "string"
        },
        "available_downloads": {
          "type": "integer"
        },
        "is_only_TVShows": {
          "type": "boolean"
        },
        "kids_mode": {
          "type": "boolean"
        },
        "is_set_pin": {
          "type": "boolean"
        },
        "uuid": {
          "type": "string"
        },
        "accepted_sport": {
          "type": "boolean"
        },
        "is_recurrent_payments": {
          "type": "boolean"
        },
        "recurrent_tariff": {
          "type": "null"
        },
        "discount": {
          "type": "null"
        },
        "recurrent_card": {
          "type": "null"
        },
        "recurrent_next_payment_date": {
          "type": "null"
        }
      },
      "required": [
        "pk",
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "avatar",
        "vk",
        "facebook",
        "telegram",
        "email_subscribe",
        "telegram_subscribe",
        "vk_subscribe",
        "facebook_subscribe",
        "is_active",
        "is_blocked",
        "is_part_blocked",
        "favorites",
        "reviews",
        "my_serials",
        "user_domain",
        "subscription",
        "user_subdomain",
        "quality_name",
        "quality_for_all",
        "phone",
        "has_obtained_films",
        "balance",
        "referrer_link",
        "available_downloads",
        "is_only_TVShows",
        "kids_mode",
        "is_set_pin",
        "uuid",
        "accepted_sport",
        "is_recurrent_payments",
        "recurrent_tariff",
        "discount",
        "recurrent_card",
        "recurrent_next_payment_date"
      ]
    },
    "refresh_token": {
      "type": "string"
    }
  },
  "required": [
    "token",
    "user",
    "refresh_token"
  ]
}
