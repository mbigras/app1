# App1

> App1 is a small flask web app for experimentation.

App1 serves as an application template for more complex web applications. It demonstrates norms and conventions that increase reliability during application delivery. For a detailed discussion on application delivery refer to this excellent Hashicorp document: [Application Delivery with HashiCorp](https://www.hashicorp.com/resources/application-delivery-hashicorp)

## Getting started

1. Build the `app1` Docker image locally

   ```
   docker build -t app1 .
   ```

1. Run the `app1` Docker container

   ```
   docker run -it -p 8080:8080 app1
   ```

   * Publish the app1 default listening port 8080 to host port 8080

1. Open a separate terminal

1. Issue an HTTP request to the root route

   ```
   curl http://localhost:8080/
   ```

   The `app1` configuration is returned as JSON. Note the `VERSION` key the see the version of `app1`.
