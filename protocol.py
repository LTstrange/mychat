# login protocol
# client:
client_login = {"protocol": "cli_login",
                "username": "username",
                "password": "password"
                }

# server:
server_login_success = {"protocol": "ser_login",
                        "result": True,
                        "user_data": {"uuid": "uuid",
                                      "username": "username"
                                      }
                        }

server_login_failure = {"protocol": "ser_login",
                        "result": False,
                        "msg": "msg"
                        }

# search protocol
# client:
client_search = {"protocol": "cli_search",
                 "uuid": "uuid"
                 }

# server:
server_search_success = {"protocol": "ser_search",
                         "result": True,
                         "user_data": ["username1",
                                       "username2",
                                       "username3"]
                         }

server_search_failure = {"protocol": "ser_search",
                         "result": False,
                         "msg": "msg"
                         }

# connect_with protocol
# client:
client_connect_with = {"protocol": "cli_connect_with",
                       "uuid": "uuid",
                       "target": "target_username"
                       }

# server:
server_connect_success = {"protocol": "ser_connect_with",
                          "result": True,
                          "target_uuid": "uuid"
                          }

server_connect_failure = {"protocol": "ser_connect_with",
                          "result": False,
                          "type": ("cannot find", "target_refuse"),
                          "msg": "msg"
                          }

# chat protocol
# client:
client_chat_send = {"protocol": "cli_chat_send",
                    "target": "target_username",
                    "send_content": "content",
                    }

# chat_receive:
client_chat_receive_success = {"protocol": "cli_chat_receive",
                               "result": True,
                               }

# server:
server_chat_send = {"protocol": "ser_chat_send",
                    "from": "username",
                    "content": "content",
                    }

server_chat_route_success = {"protocol": "ser_chat_route_check",
                             "result": True,
                             "msg": "message has been send."
                             }

server_chat_route_failure = {"protocol": "ser_chat_route_check",
                             "result": False,
                             "type": ("cannot find", "target_refuse"),
                             "msg": "msg"
                             }

# logout protocol
# TODO: 决定将退出登录的协议写在哪里
# client:
client_logout = {"protocol": "cli_logout",
                 "uuid": "uuid"}
