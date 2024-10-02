# Data Pipeline Project

This project is a data pipeline implemented using Spark and MinIO as a data lake. It provides a framework for processing and analyzing large datasets efficiently.

## Project Structure

The project has the following directory structure:

```
data-pipeline-project
├── src
│   ├── main.py
│   ├── pipelines
│   │   └── example_pipeline.py
│   └── utils
│       └── helpers.py
├── infrastructure
│   ├── docker-compose.yml
│   └── minio
│       ├── Dockerfile
│       └── config
│           └── minio_config.json
├── requirements.txt
├── setup.py
└── README.md
```

## Files

- `src/main.py`: This file is the entry point of the data pipeline project. It contains the main logic for executing the data pipelines using Spark and MinIO.

- `src/pipelines/example_pipeline.py`: This file contains an example data pipeline implemented using PySpark. It defines functions or classes that perform specific data processing tasks.

- `src/utils/helpers.py`: This file contains utility functions or classes that can be used by the data pipelines or other parts of the project.

- `infrastructure/docker-compose.yml`: This file is used for defining the Docker Compose configuration to set up the MinIO container.

- `infrastructure/minio/Dockerfile`: This file is used to build the Docker image for the MinIO container. It specifies the base image and any additional configurations or dependencies required.

- `infrastructure/minio/config/minio_config.json`: This file contains the configuration settings for the MinIO server, such as access keys, secret keys, and bucket configurations.

- `requirements.txt`: This file lists the Python dependencies required for the project. It includes packages like PySpark and any other libraries used in the data pipelines.

- `setup.py`: This file is used for packaging the project as a Python package. It includes metadata about the project and its dependencies.

## Setup and Usage

To set up the data pipeline project, follow these steps:

1. Install the required dependencies listed in `requirements.txt` by running the following command:

   ```
   pip install -r requirements.txt
   ```

2. Build the MinIO Docker image by running the following command in the `infrastructure/minio` directory:

   ```
   docker build -t minio .
   ```

3. Start the MinIO container using Docker Compose by running the following command in the `infrastructure` directory:

   ```
   docker-compose up -d
   ```

4. Run the data pipeline by executing the `main.py` script in the `src` directory:

   ```
   python main.py
   ```

   This will execute the example data pipeline defined in `pipelines/example_pipeline.py` using Spark and MinIO.

For more information on how to use and customize the data pipeline project, please refer to the documentation in the code files and the project's README.

## License

This project is licensed under the [MIT License](LICENSE).