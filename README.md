# tmd67-be
Backend api of TM D67 website. Currently based on [Django REST framework](https://www.django-rest-framework.org/) and [Strawberry GraphQL Django](https://strawberry-graphql.github.io/strawberry-graphql-django/)

## Requirements
Docker

(Recommends) Vscode with plugin [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---
## Doc
https://www.notion.so/c2caef7031e34d02873b4a40f9d47108?v=ea44cdf488634e3bbb763a72805e2a9d&p=3b491b62140344618c9a53b48324bdd5&pm=s

## Run pruduction server
Download `data.json` from `tmd67-data` repo and put it in this folder and run:

    docker-compose up -d

Then you can see the api docs via http://localhost.

GraphQL api can be viewed at http://localhost/graphql.

---
## Contributing
Thanks for the contributing! Please fork this repo to your personal repositories and contribute with pull requests.

### Set up your dev environment
If you are using Vscode and have [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed, follow the instruction of the pop-up notification and you will create a container with test environment.

If you prefer use manual env, run:

    pip install -r requirements_dev.txt

### Set up your database
By default, Dev Containers will provide a Postgres DB on localhost for testing. See [here](https://github.com/toastmasters-d67/tmd67-be/blob/main/.devcontainer/docker-compose.yml#L29) for more details such as username.

For data migration, download `data.json` from `tmd67-data` repo and put it in this folder and run:

    make migrate

### Run the test server
    make run
