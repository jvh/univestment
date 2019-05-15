const LineData = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)];

const BarData = [12, 5, 6, 6, 9, 10, 15, 5, 3];

const Filtered = [
  {
    "property" : {
      "adzuna": {
        "__CLASS__": "Adzuna::API::Response::Property",
        "adref": "eyJhbGciOiJIUzI1NiJ9.eyJpIjoxMTE0ODQ2NzYxLCJzIjoiTDM2aWZzcHpULWU4QXRJVkpUN2ZIQSJ9.aSOZYQoAZoantJMeCJLmEm26mDl1IzVZufFSZlcE0Nw",
        "beds": 1,
        "category": {
          "__CLASS__": "Adzuna::API::Response::Category",
          "label": "For Sale",
          "tag": "for-sale"
        },
        "created": "2019-03-29T14:13:56Z",
        "description": "This superb one bedroom ground floor apartment is situated in the sought after area of Millbrook and is offered with no forward chain. This is an ideal investment opportunity and could also be suited to first time buyers. The property benefits from having underfloor heating.",
        "id": 1114846761,
        "image_url": "https://s3-eu-west-1.amazonaws.com/property.adzuna.co.uk/a59e47e1c5ddd2fdfd53dd426f9f2169a471092ec1f0eaab81bc08c985e5f61f.jpeg",
        "is_furnished": "0",
        "latitude": 50.928699,
        "location": {
          "__CLASS__": "Adzuna::API::Response::Location",
          "area": [
            "UK",
            "South East England",
            "Hampshire",
            "Southampton"
          ],
          "display_name": "Southampton, Hampshire"
        },
        "longitude": -1.44911,
        "postcode": "SO164PU",
        "property_type": "flat",
        "redirect_url": "https://property.adzuna.co.uk/land/ad/1114846761?se=L36ifspzT-e8AtIVJT7fHA&utm_medium=api&utm_source=d1b12649&v=65068C80F9B11360879A34F9D8046DF278E1CBFF",
        "sale_price": 100000,
        "title": "1 bed flat for sale in Wimpson Lane"
      },
      "investment":{
        "market_value": 130000
      }
    },
    "historic_data": {
      "outcode": {
        "historic": {
          "x":[0,1,3,4,5,7,8,9,10],
          "y":[13,24,46,68,89,102,114]
        },
        "predicted": {
          "x":[11,12,13,14,15,17,19],
          "y":[123,124,146,168,189,202,214]
        }
      }
    }
  }];

export { LineData, BarData, Filtered };
