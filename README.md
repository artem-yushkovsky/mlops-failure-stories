# MLOps Failure Stories

A compiled list of links to public failure stories related to Kubernetes.
Most recent publications on top.

* [Why we switched from fluent-bit to Fluentd in 2 hours - PrometheusKube - blog post 2020](https://prometheuskube.com/why-we-switched-from-fluent-bit-to-fluentd-in-2-hours) 
    * involved: fluent-bit, missing logs, Fluentd
    * impact: lost application logs in production

# Why

Kubernetes is a fairly complex system with many moving parts.
Its ecosystem is constantly evolving and adding even more layers (service mesh, ...) to the mix.
Considering this environment, we don't hear enough real-world horror stories to learn from each other!
This compilation of failure stories should make it easier for people dealing with Kubernetes operations (SRE, Ops, platform/infrastructure teams) to
learn from others and reduce the unknown unknowns of running Kubernetes in production.
For more information, [see the blog post](https://srcco.de/posts/mlops-failure-stories.html).

# Contributing

Please help the community and **[share a link to your failure story by opening a Pull Request!](https://codeberg.org/hjacobs/mlops-failure-stories/_edit/main/README.md)**
Failure stories can be anything like blog posts, conference/meetup talks, incident postmortems, tweetstorms, ...

I would also be glad to hear about your failure stories on Twitter: my handle is [@try_except_](https://twitter.com/try_except_)

# Thanks

Thanks to all contributors and everybody who writes public Kubernetes postmortems! 👏

Thanks to [Joe Beda](https://twitter.com/jbeda) for contributing his domain k8s.af for this project! 👏
