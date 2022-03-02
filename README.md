# App1

> App1 is a Flask web application for practice.

App1 is for practicing [application delivery](https://www.hashicorp.com/resources/application-delivery-hashicorp).

## Getting started

1. Build the `app1` Docker image.

   ```
   docker build -t app1 .
   ```

1. Run the `app1` Docker container.

   ```
   docker run --rm -it -p 8080:8080 -e FOO=fortytwo app1
   ```

   Consider the following options:
   * `--rm `: Ensure the container is cleaned up when stopped.
   * `-it`: Run App1 in the foreground.
   * `-p 8080:8080`: Publish the App1 default listening port 8080 to host port 8080.
   * `-e FOO=fortytwo`: Configure the foo setting.

1. Open a separate terminal.

1. Send an HTTP GET request.

   ```
   curl http://localhost:8080/
   ```

   The `app1` configuration is returned as JSON.

1. Navigate back to the terminal where App1 is running.

1. Shutdown App1.

   Press `ctrl`+`c`.
