# File upload server

_Simple file upload server for testing_

## Usage

```
$ docker run -it -p 5000:5000 ghcr.io/andreasjansson/docker-file-upload-server:main
```

Then you can send files to the server:

```
$ echo hello world > my-file.txt
$ curl -X PUT http://localhost:5000/upload -F "file=@my-file.txt"

{
  "url": "http://07cbecfea60c:5000/download/my-file.txt"
}
```

The file is available to download at `/download/my-file.txt`:

```
$ curl http://localhost:5000/download/my-file.txt

hello world
```

You can also save downloaded files to the file system my mounting `/uploads` from the container onto the host:

```
docker run -it -v -p 5000:5000 ghcr.io/andreasjansson/docker-file-upload-server:main
```

And in a new shell:

```
$ echo hello world > my-file.txt
$ curl -X PUT http://localhost:5000/upload -F "file=@my-file.txt"

{
  "url": "http://07cbecfea60c:5000/download/my-file.txt"
}

$ cat uploaded-files/my-file.txt

hello world
```
