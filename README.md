
![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Pizza_slice.png/220px-Pizza_slice.png)

    
#  Pizza Api

Using CRUD operation on API 

## Documentation

This API uses some endpoint and there are some request which I will be describing here.
`Database used here is mongodb database name is pizzadatabase`

| Description                       |
| :-------------------------------- |
| **Create** : To create a pizza with specified format in API |
|**Request** : GET & POST|

`e.g POST http://127.0.0.1:8000/create-pizza/ = will create new pizza`

| Description                       |
| :-------------------------------- |
| **ListPizza's** : To List all pizza with in API |
|**Request** : GET & PUT|

`e.g POST http://127.0.0.1:8000/create-pizza/ = will create new pizza`

`e.g GET http://127.0.0.1:8000/list-pizza=0/ = will list all pizza`

| Description                       |
| :-------------------------------- |
| **Create** : To list specific pizza with specified format in API |
|**Request** : GET |

`e.g GET http://127.0.0.1:8000/list-pizza-{value}={subnameofvalue} = will list pizza with specific subnameofvalue`



  
## API Reference

#### Create pizza with all details 

```http
  GET http://127.0.0.1:8000/create-pizza/
```

| Description                       |
| :-------------------------------- |
| **Required**: To create a pizza with specified format in API |

```
As create is using post request to create new pizza.

POST http://127.0.0.1:8000/create-pizza/

Enter the detailed JSON response in body and post to go with flow and add new pizza to database.

```
#### List all PIZZA'S

```http
  GET http://127.0.0.1:8000/list-pizza=0
```
| Description                       |
| :-------------------------------- |
| **Required**: To List all pizza with in API |

`Here 0 is assigned to list-pizza purposly to list all the pizza's`
```
Will get all the list of pizza's to be ordered.
```
```
Handling a PUT request in List 

PUT http://127.0.0.1:8000/list-pizza={id}

The most important thing is id here I have taken that id is never 0 so 
when id is replaced by 0 then it will display all the pizza list otherwise it will update the pizza list 
```

#### List specified pizza's based on :)
```
```http
  GET http://127.0.0.1:8000/list-pizza-topping={nameoftopping}
```
`type(Regular or Square),size(Small,Large,Medium,Extra-Large),toppings(any)`

`list-pizza-{value}={nameofval} ,{value}:(Type,Size,Topping) {nameofval}:depends on which name is consider `
| Description                       |
| :-------------------------------- |
| **Required**: To specify a pizza on basis of criteria given by {value} and {nameofval} |

`Here 0 is assigned to list-pizza purposly to list all the pizza's`




  
## Installation of module

Install all the present in requirements.txt

```bash 
  pip install -r requirements.txt
```
    
## Authors

- [@omkarhalgi](https://github.com/OMH-G/CodeLength)

  