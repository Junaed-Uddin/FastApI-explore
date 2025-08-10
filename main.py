from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def about():
    return {
        "data": {
            "Name": "Junaed",
            "Designation": "Trainee - Software Engineer",
            "Salary": 8000,
            "Company": "ADN Diginet"
        }
    }
    
    
@app.get("/blogs")
def blogs():
    return {
        "data":{
            "Name": "Tech Valley",
            "Publisher Name": "Junaed",
            "Category": "Technology",
            "time": "10.00 am",
        }
    }
    
    
@app.get("/blogs/{blog_id}")
def single_blog(blog_id):
    return{
        "data": f"Blog {blog_id} published successfully"
    }
