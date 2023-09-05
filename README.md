# Streaming Framework
A networking framework to receive public posts from one or more Mastodon user accounts and publish the posts onto different channels in near realtime. It also provides data pipelines to perform data analysis of the user activity based on the recceived posts.


# Software Design Phase

## Phase-1: Proof of concept
 - Simple monolith software architecure capable of
   - receiving posts from a single Mastodon account
   - publish the post on a given account
  
## Phase-2: MVP (minimum viable product)
 - Single system modular monolithic implementation with Kafka
 - Contains only one producer
 - Two consumer groups
   - each group contains one consumer

## Phase-3: Scalable software architecture

```Work In Progress!!!```

Expected to fulfill the following functional requirements:
 - Receives posts from different user accounts
 - Provides different types of output channels for 
   - publishing received posts
   - publishing different user stats

![application architecture](./docs/app_arch.jpg)


# How To

