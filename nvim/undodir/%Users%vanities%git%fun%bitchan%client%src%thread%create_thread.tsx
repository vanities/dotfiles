Vim�UnDo� ��⥙��3y �(�ߚBN �{�    6   Limport { Container, Col, Button, Form, FormGroup, Input } from "reactstrap";                             ^���    _�                            ����                                                                                                                                                                                                                                                                                                                                                             ^�     �                    console.log("asdaadsd");5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��     �         =      /export function CreateThread (props, context) {5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��     �         =      ,export const CreateThread (props, context) {5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             ^��    �         =      .export const CreateThread = (props, context) {5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             ^��    �   <   >          }�   ;   =            );�   :   <          
    </div>�   9   ;                </Container>�   8   :                  </Form>�   7   9          !          <Button>Submit</Button>�   6   8                    </Col>�   5   7                      </FormGroup>�   4   6                        />�   3   5          $                value={values.image}�   2   4          ,                onChange={handleInputChange}�   1   3          #                placeholder="image"�   0   2                          name="image"�   /   1                          type="text"�   .   0                        <Input�   -   /                        />�   ,   .          #                value={values.text}�   +   -          ,                onChange={handleInputChange}�   *   ,          "                placeholder="text"�   )   +                          name="text"�   (   *                          type="text"�   '   )                        <Input�   &   (                        />�   %   '          &                value={values.subject}�   $   &          ,                onChange={handleInputChange}�   #   %          %                placeholder="subject"�   "   $                          name="subject"�   !   #                          type="text"�       "                        <Input�      !                      <FormGroup>�                           <Col>�                           <h3>post a thread</h3>�                &        <Form onSubmit={handleSubmit}>�                *      <Container className="createthread">�                &      Total # of Threads: {numThreads}�                	    <div>�                
  return (�                 �                M  const [values, setValues] = useState({ subject: "", text: "", image: "" });�                  };�                    event.preventDefault();�                4    send(values.subject, values.text, values.image);�                #  const handleSubmit = (event) => {�                 �                  };�                ,    setValues({ ...values, [name]: value });�                %    const { name, value } = e.target;�                $  const handleInputChange = (e) => {�                 �                2  const numThreads = state ? state[0] : "loading";�   
             7  const state = useCacheCall("Bitchan", "threadCount");�   	              �      
          ;  const { send } = useCacheSend("Bitchan", "createThread");�      	          <  // const threads = useCacheCall("Bitchan", "lastThreads");�                H  const { useCacheCall, useCacheSend } = drizzleReactHooks.useDrizzle();�                1export const CreateThread = (props, context) => {�                 �                :import { drizzleReactHooks } from "@drizzle/react-plugin";�                Limport { Container, Col, Button, Form, FormGroup, Input } from "reactstrap";�                !import { useState } from "react";�                 import * as React from "react";5�_�                           ����                                                                                                                                                                                                                                                                                                                            	   .          .       V   .    ^��     �                <  // const threads = useCacheCall("Bitchan", "lastThreads");5�_�      	              
        ����                                                                                                                                                                                                                                                                                                                            
                      V        ^��     �   	   
          7  const state = useCacheCall("Bitchan", "threadCount");   2  const numThreads = state ? state[0] : "loading";5�_�      
          	          ����                                                                                                                                                                                                                                                                                                                                                v       ^��    �                &      Total # of Threads: {numThreads}5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                v       ^��    �   8              };�   7   9            );�   6   8          
    </div>�   5   7                </Container>�   4   6                  </Form>�   3   5          !          <Button>Submit</Button>�   2   4                    </Col>�   1   3                      </FormGroup>�   0   2                        />�   /   1          $                value={values.image}�   .   0          ,                onChange={handleInputChange}�   -   /          #                placeholder="image"�   ,   .                          name="image"�   +   -                          type="text"�   *   ,                        <Input�   )   +                        />�   (   *          #                value={values.text}�   '   )          ,                onChange={handleInputChange}�   &   (          "                placeholder="text"�   %   '                          name="text"�   $   &                          type="text"�   #   %                        <Input�   "   $                        />�   !   #          &                value={values.subject}�       "          ,                onChange={handleInputChange}�      !          %                placeholder="subject"�                                 name="subject"�                                type="text"�                              <Input�                            <FormGroup>�                          <Col>�                           <h3>post a thread</h3>�                &        <Form onSubmit={handleSubmit}>�                *      <Container className="createthread">�                	    <div>�                
  return (�                 �                M  const [values, setValues] = useState({ subject: "", text: "", image: "" });�                  };�                    event.preventDefault();�                4    send(values.subject, values.text, values.image);�                #  const handleSubmit = (event) => {�                 �                  };�                ,    setValues({ ...values, [name]: value });�                %    const { name, value } = e.target;�   
             $  const handleInputChange = (e) => {�   	              �      
           �      	          ;  const { send } = useCacheSend("Bitchan", "createThread");�                H  const { useCacheCall, useCacheSend } = drizzleReactHooks.useDrizzle();�                1export const CreateThread = (props, context) => {�                 �                :import { drizzleReactHooks } from "@drizzle/react-plugin";�                Limport { Container, Col, Button, Form, FormGroup, Input } from "reactstrap";�                !import { useState } from "react";�                 import * as React from "react";5�_�   
                    
    ����                                                                                                                                                                                                                                                                                                                                                v       ^�    �         8      H  const { useCacheCall, useCacheSend } = drizzleReactHooks.useDrizzle();5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                v       ^�    �   7   9          };�   6   8            );�   5   7          
    </div>�   4   6                </Container>�   3   5                  </Form>�   2   4          !          <Button>Submit</Button>�   1   3                    </Col>�   0   2                      </FormGroup>�   /   1                        />�   .   0          $                value={values.image}�   -   /          ,                onChange={handleInputChange}�   ,   .          #                placeholder="image"�   +   -                          name="image"�   *   ,                          type="text"�   )   +                        <Input�   (   *                        />�   '   )          #                value={values.text}�   &   (          ,                onChange={handleInputChange}�   %   '          "                placeholder="text"�   $   &                          name="text"�   #   %                          type="text"�   "   $                        <Input�   !   #                        />�       "          &                value={values.subject}�      !          ,                onChange={handleInputChange}�                 %                placeholder="subject"�                                name="subject"�                                type="text"�                              <Input�                            <FormGroup>�                          <Col>�                           <h3>post a thread</h3>�                &        <Form onSubmit={handleSubmit}>�                *      <Container className="createthread">�                	    <div>�                
  return (�                 �                M  const [values, setValues] = useState({ subject: "", text: "", image: "" });�                  };�                    event.preventDefault();�                4    send(values.subject, values.text, values.image);�                #  const handleSubmit = (event) => {�                 �                  };�                ,    setValues({ ...values, [name]: value });�   
             %    const { name, value } = e.target;�   	             $  const handleInputChange = (e) => {�      
           �      	          ;  const { send } = useCacheSend("Bitchan", "createThread");�                ;  const {  useCacheSend } = drizzleReactHooks.useDrizzle();�                1export const CreateThread = (props, context) => {�                 �                :import { drizzleReactHooks } from "@drizzle/react-plugin";�                Limport { Container, Col, Button, Form, FormGroup, Input } from "reactstrap";�                !import { useState } from "react";�                 import * as React from "react";5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                V       ^�({     �         8    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ^�(|     �      	   9    �         9    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ^�(}     �                 5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                V       ^�(�     �         9      +  const { buttonLabel, className } = props;5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                V       ^�(�    �         9        const {} = props;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ^�(�   	 �         9      !  const { handleSubmit } = props;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ^�(�   
 �   8   :          };�   7   9            );�   6   8          
    </div>�   5   7                </Container>�   4   6                  </Form>�   3   5          !          <Button>Submit</Button>�   2   4                    </Col>�   1   3                      </FormGroup>�   0   2                        />�   /   1          $                value={values.image}�   .   0          ,                onChange={handleInputChange}�   -   /          #                placeholder="image"�   ,   .                          name="image"�   +   -                          type="text"�   *   ,                        <Input�   )   +                        />�   (   *          #                value={values.text}�   '   )          ,                onChange={handleInputChange}�   &   (          "                placeholder="text"�   %   '                          name="text"�   $   &                          type="text"�   #   %                        <Input�   "   $                        />�   !   #          &                value={values.subject}�       "          ,                onChange={handleInputChange}�      !          %                placeholder="subject"�                                 name="subject"�                                type="text"�                              <Input�                            <FormGroup>�                          <Col>�                           <h3>post a thread</h3>�                &        <Form onSubmit={handleSubmit}>�                *      <Container className="createthread">�                	    <div>�                
  return (�                 �                M  const [values, setValues] = useState({ subject: "", text: "", image: "" });�                  };�                    event.preventDefault();�                4    send(values.subject, values.text, values.image);�                #  const handleSubmit = (event) => {�                 �                  };�                ,    setValues({ ...values, [name]: value });�                %    const { name, value } = e.target;�   
             $  const handleInputChange = (e) => {�   	              �      
          ;  const { send } = useCacheSend("Bitchan", "createThread");�      	          :  const { useCacheSend } = drizzleReactHooks.useDrizzle();�                #  //const { handleSubmit } = props;�                1export const CreateThread = (props, context) => {�                 �                :import { drizzleReactHooks } from "@drizzle/react-plugin";�                Limport { Container, Col, Button, Form, FormGroup, Input } from "reactstrap";�                !import { useState } from "react";�                 import * as React from "react";5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ^�*�    �         9      &        <Form onSubmit={handleSubmit}>5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ^�+      �         9      7        <Form id="creatthread" onSubmit={handleSubmit}>5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ^�+    �         9      7        <Form id="createhread" onSubmit={handleSubmit}>5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                V       ^�+8    �                           <h3>post a thread</h3>5�_�                    3   
    ����                                                                                                                                                                                                                                                                                                                                                V       ^�+E    �   2   3          !          <Button>Submit</Button>5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��E    �                $  // const { handleSubmit } = props;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^���    �         6      Limport { Container, Col, Button, Form, FormGroup, Input } from "reactstrap";5�_�              	             ����                                                                                                                                                                                                                                                                                                                                                v       ^��     �         :      %    <dival # of Threads: {numThreads}5��