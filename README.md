# Routinghub Routing API examples

## Introduction
This repository contains up-to-date examples of various route optimization
tasks in Routinghub Routing API JSON format, and an example API client.

The documentation for Routing API is available at:

`devel` branch:
https://routinghub.com/api/routing/v1-devel/doc

`stable` branch:
https://routinghub.com/api/routing/v1/doc

## Prerequisities
A recent version of Python3 and `requests` package is required to run examples.
All command line snippents below assume Linux or Darwin environment.

## API client
A simple API client can be found at `example-client.py`. Note, that the only
purpose of this client script is to demonstrate asynchronous requests to Routing API -
the provided client does not handle HTTP retries and possible network errors, which
is a must-do in production setting.

By default, API client uses `devel` API endpoint, which is suitable for
experiments and has all capabilities of `stable` (production) endpoint,
plus new features that have not been stabilized yet.

## Running examples
To run an example:
```
$ export APIKEY=<your API key>
$ cat basic1.example.json | ./example-client.py > basic1.response.json
```

The example API client reads optimization requests from `stdin`, submits it
to Routing API, waits for succesful completion, and writes output JSON to `stdout`.

## Debugging requests
During initial setup of constraints and cost function, it is recommended to run 
optimization in `debug` mode, see [`request.options.quality`](https://routinghub.com/api/routing/v1-devel/doc#addRoutingRequest.request.options.quality)

## Analyzing results
Please note that optimization search algorithm is stochastic,
and can produce different results for the same optimization task
for several runs.

When designing cost models or experimenting with parameters, it is recommended
to compare results statistically across several runs, by calculating p-value
or another statistical measure of your choice.

## Developer support
We provide free developer's support over Slack, please email us at [support@routinghub.com](mailto:support@routinghub.com)
for the access.

Along with any technical question, we can help you build optimization for your business case,
or implement additional functionality not covered by the API schema yet.


