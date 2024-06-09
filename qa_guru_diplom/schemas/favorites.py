post_favorites = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "film": {
      "type": "object",
      "properties": {
        "original_name": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "original_name",
        "year",
        "genre"
      ]
    },
    "img": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "kp": {
      "type": "string"
    },
    "imdb": {
      "type": "string"
    },
    "rating": {
      "type": "string"
    },
    "likes": {
      "type": "integer"
    },
    "dislikes": {
      "type": "integer"
    },
    "favorite": {
      "type": "boolean"
    },
    "review": {
      "type": "boolean"
    },
    "like": {
      "type": "null"
    },
    "dislike": {
      "type": "null"
    },
    "series": {
      "type": "integer"
    },
    "slug": {
      "type": "string"
    },
    "scheel": {
      "type": "array",
      "items": {}
    },
    "season": {
      "type": "integer"
    },
    "novelty_image": {
      "type": "string"
    },
    "start": {
      "type": "object",
      "properties": {
        "season": {
          "type": "integer"
        },
        "series": {
          "type": "integer"
        }
      },
      "required": [
        "season",
        "series"
      ]
    },
    "categories": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "mobile_baner_slider": {
      "type": "boolean"
    },
    "mobile_baner_image": {
      "type": "null"
    },
    "is_film": {
      "type": "boolean"
    },
    "backdrop_mini": {
      "type": "string"
    },
    "poster_middle": {
      "type": "string"
    },
    "is_free": {
      "type": "boolean"
    },
    "is_my": {
      "type": "boolean"
    },
    "synonyms": {
      "type": "string"
    },
    "announcement": {
      "type": "boolean"
    },
    "announcement_time": {
      "type": "null"
    },
    "is_available": {
      "type": "boolean"
    },
    "timeline": {
      "type": "integer"
    },
    "timeline_info": {
      "type": "null"
    },
    "available_with_advertise_all": {
      "type": "boolean"
    },
    "min_age": {
      "type": "integer"
    },
    "year": {
      "type": "integer"
    },
    "duration": {
      "type": "string"
    },
    "countries": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "newest_trailer": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "film",
    "img",
    "name",
    "kp",
    "imdb",
    "rating",
    "likes",
    "dislikes",
    "favorite",
    "review",
    "like",
    "dislike",
    "series",
    "slug",
    "scheel",
    "season",
    "novelty_image",
    "start",
    "categories",
    "mobile_baner_slider",
    "mobile_baner_image",
    "is_film",
    "backdrop_mini",
    "poster_middle",
    "is_free",
    "is_my",
    "synonyms",
    "announcement",
    "announcement_time",
    "is_available",
    "timeline",
    "timeline_info",
    "available_with_advertise_all",
    "min_age",
    "year",
    "duration",
    "countries",
    "newest_trailer"
  ]
}

get_favorites = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "count": {
      "type": "integer"
    },
    "next": {
      "type": "null"
    },
    "previous": {
      "type": "null"
    },
    "results": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "film": {
              "type": "object",
              "properties": {
                "original_name": {
                  "type": "string"
                },
                "year": {
                  "type": "integer"
                },
                "genre": {
                  "type": "string"
                }
              },
              "required": [
                "original_name",
                "year",
                "genre"
              ]
            },
            "img": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "kp": {
              "type": "string"
            },
            "imdb": {
              "type": "string"
            },
            "rating": {
              "type": "string"
            },
            "likes": {
              "type": "integer"
            },
            "dislikes": {
              "type": "integer"
            },
            "favorite": {
              "type": "boolean"
            },
            "review": {
              "type": "boolean"
            },
            "like": {
              "type": "null"
            },
            "dislike": {
              "type": "null"
            },
            "series": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "scheel": {
              "type": "array",
              "items": {}
            },
            "season": {
              "type": "integer"
            },
            "novelty_image": {
              "type": "string"
            },
            "start": {
              "type": "object",
              "properties": {
                "season": {
                  "type": "integer"
                },
                "series": {
                  "type": "integer"
                }
              },
              "required": [
                "season",
                "series"
              ]
            },
            "categories": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "mobile_baner_slider": {
              "type": "boolean"
            },
            "mobile_baner_image": {
              "type": "null"
            },
            "is_film": {
              "type": "boolean"
            },
            "backdrop_mini": {
              "type": "string"
            },
            "poster_middle": {
              "type": "string"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_my": {
              "type": "boolean"
            },
            "synonyms": {
              "type": "string"
            },
            "announcement": {
              "type": "boolean"
            },
            "announcement_time": {
              "type": "null"
            },
            "is_available": {
              "type": "boolean"
            },
            "timeline": {
              "type": "integer"
            },
            "timeline_info": {
              "type": "null"
            },
            "available_with_advertise_all": {
              "type": "boolean"
            },
            "min_age": {
              "type": "integer"
            },
            "year": {
              "type": "integer"
            },
            "duration": {
              "type": "string"
            },
            "countries": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                }
              ]
            },
            "newest_trailer": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "film",
            "img",
            "name",
            "kp",
            "imdb",
            "rating",
            "likes",
            "dislikes",
            "favorite",
            "review",
            "like",
            "dislike",
            "series",
            "slug",
            "scheel",
            "season",
            "novelty_image",
            "start",
            "categories",
            "mobile_baner_slider",
            "mobile_baner_image",
            "is_film",
            "backdrop_mini",
            "poster_middle",
            "is_free",
            "is_my",
            "synonyms",
            "announcement",
            "announcement_time",
            "is_available",
            "timeline",
            "timeline_info",
            "available_with_advertise_all",
            "min_age",
            "year",
            "duration",
            "countries",
            "newest_trailer"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "film": {
              "type": "object",
              "properties": {
                "original_name": {
                  "type": "string"
                },
                "year": {
                  "type": "integer"
                },
                "genre": {
                  "type": "string"
                }
              },
              "required": [
                "original_name",
                "year",
                "genre"
              ]
            },
            "img": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "kp": {
              "type": "string"
            },
            "imdb": {
              "type": "string"
            },
            "rating": {
              "type": "string"
            },
            "likes": {
              "type": "integer"
            },
            "dislikes": {
              "type": "integer"
            },
            "favorite": {
              "type": "boolean"
            },
            "review": {
              "type": "boolean"
            },
            "like": {
              "type": "null"
            },
            "dislike": {
              "type": "null"
            },
            "series": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "scheel": {
              "type": "array",
              "items": {}
            },
            "season": {
              "type": "integer"
            },
            "novelty_image": {
              "type": "string"
            },
            "start": {
              "type": "object",
              "properties": {
                "season": {
                  "type": "integer"
                },
                "series": {
                  "type": "integer"
                }
              },
              "required": [
                "season",
                "series"
              ]
            },
            "categories": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "mobile_baner_slider": {
              "type": "boolean"
            },
            "mobile_baner_image": {
              "type": "null"
            },
            "is_film": {
              "type": "boolean"
            },
            "backdrop_mini": {
              "type": "string"
            },
            "poster_middle": {
              "type": "string"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_my": {
              "type": "boolean"
            },
            "synonyms": {
              "type": "string"
            },
            "announcement": {
              "type": "boolean"
            },
            "announcement_time": {
              "type": "null"
            },
            "is_available": {
              "type": "boolean"
            },
            "timeline": {
              "type": "integer"
            },
            "timeline_info": {
              "type": "null"
            },
            "available_with_advertise_all": {
              "type": "boolean"
            },
            "min_age": {
              "type": "integer"
            },
            "year": {
              "type": "integer"
            },
            "duration": {
              "type": "string"
            },
            "countries": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                }
              ]
            },
            "newest_trailer": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "film",
            "img",
            "name",
            "kp",
            "imdb",
            "rating",
            "likes",
            "dislikes",
            "favorite",
            "review",
            "like",
            "dislike",
            "series",
            "slug",
            "scheel",
            "season",
            "novelty_image",
            "start",
            "categories",
            "mobile_baner_slider",
            "mobile_baner_image",
            "is_film",
            "backdrop_mini",
            "poster_middle",
            "is_free",
            "is_my",
            "synonyms",
            "announcement",
            "announcement_time",
            "is_available",
            "timeline",
            "timeline_info",
            "available_with_advertise_all",
            "min_age",
            "year",
            "duration",
            "countries",
            "newest_trailer"
          ]
        }
      ]
    }
  },
  "required": [
    "count",
    "next",
    "previous",
    "results"
  ]
}
