# pylint: disable=import-error
from db import user_tab
from logic import crawl_trending
from fastapi import FastAPI, status, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import mangum



app = FastAPI()
basic_auth = HTTPBasic()


@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(credentials: HTTPBasicCredentials):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="missing credentials"
        )

    # create user
    user = dict(
        user_id=str(uuid4()),
        username=credentials.username,
        password=generate_password_hash(credentials.password),
    )

    resp = user_tab.put_item(Item=user)
    if resp["ResponseMetadata"]["HTTPStatusCode"] != 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="something went wrong"
        )

    return {"message": "user registered", "id": f"{user['user_id']}"}


@app.post("/crawl", status_code=status.HTTP_200_OK)
async def crawl(user_id: str, credentials: HTTPBasicCredentials = Depends(basic_auth)):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="missing credentials"
        )

    get_resp = user_tab.get_item(Key={"user_id": user_id})
    if get_resp["ResponseMetadata"]["HTTPStatusCode"] != 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exist"
        )

    db_usr = get_resp["Item"]["username"] == str(credentials.username)
    if not db_usr and check_password_hash(
        get_resp["Item"]["username"], credentials.password
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid credentials"
        )
    products, err = crawl_trending()
    if products is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"something went wrong, {err}",
        )
    return products


# if __name__ == "__main__":
#     uvicorn.run("app:app", port=8001, reload=True)


lambda_handler = mangum.Mangum(app=app, lifespan="off")
