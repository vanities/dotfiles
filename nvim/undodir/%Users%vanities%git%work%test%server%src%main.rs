Vim�UnDo� �d���8��O��O�<-�)c3P�nÏ�&   2   8        Ok(_) => print!("{} contains:\n{}", display, s),   !   '                       \g��    _�                       4    ����                                                                                                                                                                                                                                                                                                                                                             \g�    �         %      @    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \g�p     �          &       �          %    5�_�                            ����                                                                                                                                                                                                                                                                                                                                       4           V        \g�t    �             &       use std::io::prelude::*;   use std::net::TcpStream;   use std::net::TcpListener;   use std::fs::File;       fn main() {   @    let listener = TcpListener::bind("127.0.0.1:5005").unwrap();       '    for stream in listener.incoming() {   %        let stream = stream.unwrap();       "        handle_connection(stream);       }   }       -fn handle_connection(mut stream: TcpStream) {       let mut buffer = [0; 512];   &    stream.read(&mut buffer).unwrap();       $    let get = b"GET / HTTP/1.1\r\n";       >    let (status_line, filename) = if buffer.starts_with(get) {   1        ("HTTP/1.1 200 OK\r\n\r\n", "hello.html")       } else {   6        ("HTTP/1.1 404 NOT FOUND\r\n\r\n", "404.html")       };       1    let mut file = File::open(filename).unwrap();   %    let mut contents = String::new();       0    file.read_to_string(&mut contents).unwrap();       :    let response = format!("{}{}", status_line, contents);       /    stream.write(response.as_bytes()).unwrap();       stream.flush().unwrap();   }5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        \g��     �                �             5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                 v   &    \g��     �               fn get5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                 v   &    \g�     �               fn get_log(filename)5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                 v   &    \g�     �      	         fn get_log(filename: String)5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                      	           v   &    \g�'     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                      
           v   &    \g�U     �      '             �      	       5�_�                    &        ����                                                                                                                                                                                                                                                                                                                            &           '           V        \g�s     �   %   &               5�_�                    $        ����                                                                                                                                                                                                                                                                                                                            $           $           V        \g�w     �   #   %   0      }5�_�                            ����                                                                                                                                                                                                                                                                                                                            $           $           V        \g��     �                fn main() {5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �                    use std::error::Error;   use std::fs::File;   use std::io::prelude::*;   use std::path::Path;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �          +    5�_�                            ����                                                                                                                                                                                                                                                                                                                            	          	          V       \g��     �          ,    5�_�                            ����                                                                                                                                                                                                                                                                                                                            
          
          V       \g��     �         -    �         -    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �         1          use std::error::Error;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �         0    5�_�                    (        ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �   (   *   1    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �         2    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �                 5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                V       \g��     �         2      &    let path = Path::new("hello.txt");5�_�                           ����                                                                                                                                                                                                                                                                                                                                              V       \g��     �         2      !    let path = Path::new(filena);5�_�                     !   '    ����                                                                                                                                                                                                                                                                                                                                              V       \g��    �       "   2      8        Ok(_) => print!("{} contains:\n{}", display, s),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        \g�     �                �                   fn g5�_�                       )    ����                                                                                                                                                                                                                                                                                                                                                             \g�     �         %      >    let listener = TcpListener::bind(''.0.0.1:7878").unwrap();5�_�                        '    ����                                                                                                                                                                                                                                                                                                                                                             \g�     �         %      =    let listener = TcpListener::bind('.0.0.1:7878").unwrap();5��