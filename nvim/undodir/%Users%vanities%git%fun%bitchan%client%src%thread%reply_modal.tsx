Vim�UnDo� /�ؼ\$��t���ʪ/�\Ԥ������7   6   0          <Reply indexLastReply={indexThread} />   )                          _ը    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _2�     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _2�     �                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _2�     �         ;      -export const CreateThreadModal = (props) => {5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             _3     �         ;      /import { CreateThread } from "./create_thread";5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             _3     �         ;      #import {  } from "./create_thread";5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _3     �         ;      (import { Reply } from "./create_thread";5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _3    �         ;      import { Reply } from "./";5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             _3     �   :   <          };�   9   ;            );�   8   :          
    </div>�   7   9                </Modal>�   6   8                  </ModalFooter>�   5   7                    </Button>�   4   6                      Cancel�   3   5          5          <Button color="secondary" onClick={toggle}>�   2   4                    </Button>{" "}�   1   3                      Submit�   0   2                    >�   /   1                      onClick={toggle}�   .   0                      form="createthread"�   -   /                      type="submit"�   ,   .                      color="primary"�   +   -                    <Button�   *   ,                  <ModalFooter>�   )   +                  </ModalBody>�   (   *                    <CreateThread />�   '   )                  <ModalBody>�   &   (                  </ModalHeader>�   %   '                    create a thread�   $   &          6        <ModalHeader toggle={toggle} close={closeBtn}>�   #   %                >�   "   $          #        external={externalCloseBtn}�   !   #                  className={className}�       "                  toggle={toggle}�      !                  isOpen={modal}�                       <Modal�                5      <Button onClick={toggle}>{buttonLabel}</Button>�                '    <div className="createthreadmodal">�                
  return (�                  );�                    </button>�                      &times;�                /    <button className="close" onClick={toggle}>�                  const closeBtn = (�                  );�                    </button>�                      &times;�                    >�                      onClick={toggle}�                B      style={{ position: "absolute", top: "15px", right: "15px" }}�                      className="close"�                    <button�                  const externalCloseBtn = (�                 �                (  const toggle = () => setModal(!modal);�   
              �   	             ,  const [modal, setModal] = useState(false);�      
           �      	          +  const { buttonLabel, className } = props;�                &export const ReplyModal = (props) => {�                 �                 import { Reply } from "./reply";�                #import "./create_thread_modal.css";�                 �                Pimport { Button, Modal, ModalHeader, ModalBody, ModalFooter } from "reactstrap";�                 (import React, { useState } from "react";5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             _3A     �         ;      '    <div className="createthreadmodal">5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             _3B     �         ;          <div className="modal">5�_�   
                 )       ����                                                                                                                                                                                                                                                                                                                                                             _3N     �   (   *   ;                <CreateThread />5�_�                    )       ����                                                                                                                                                                                                                                                                                                                                                             _3O    �   (   *   ;                < />5�_�                    &   
    ����                                                                                                                                                                                                                                                                                                                                                             _3U     �   %   '   ;                create a thread5�_�                    &   
    ����                                                                                                                                                                                                                                                                                                                                                             _3U    �   %   '   ;      
          5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             _3�     �         ;      #import "./create_thread_modal.css";5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             _3�     �         ;      import "./_thread_modal.css";5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             _3�    �         ;      import "./_modal.css";5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _6�     �      	   ;      )  const {buttonLabel, className} = props;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _6�    �      	   ;      +  const {buttonLabel, className, } = props;5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             _6�    �   :   <          };�   9   ;            );�   8   :          
    </div>�   7   9                </Modal>�   6   8                  </ModalFooter>�   5   7                    </Button>�   4   6                      Cancel�   3   5          5          <Button color="secondary" onClick={toggle}>�   2   4                    </Button>{" "}�   1   3                      Submit�   0   2                    >�   /   1                      onClick={toggle}�   .   0                      form="createthread"�   -   /                      type="submit"�   ,   .                      color="primary"�   +   -                    <Button�   *   ,                  <ModalFooter>�   )   +                  </ModalBody>�   (   *                    <Reply />�   '   )                  <ModalBody>�   &   (                  </ModalHeader>�   %   '                    reply�   $   &          6        <ModalHeader toggle={toggle} close={closeBtn}>�   #   %                >�   "   $          #        external={externalCloseBtn}�   !   #                  className={className}�       "                  toggle={toggle}�      !                  isOpen={modal}�                       <Modal�                5      <Button onClick={toggle}>{buttonLabel}</Button>�                     <div className="replymodal">�                
  return (�                  );�                    </button>�                      &times;�                /    <button className="close" onClick={toggle}>�                  const closeBtn = (�                  );�                    </button>�                      &times;�                    >�                      onClick={toggle}�                @      style={{position: "absolute", top: "15px", right: "15px"}}�                      className="close"�                    <button�                  const externalCloseBtn = (�                 �                (  const toggle = () => setModal(!modal);�   
              �   	             ,  const [modal, setModal] = useState(false);�      
           �      	          :  const {buttonLabel, className, indexLastReply } = props;�                &export const ReplyModal = (props) => {�                 �                import {Reply} from "./reply";�                import "./reply_modal.css";�                 �                Nimport {Button, Modal, ModalHeader, ModalBody, ModalFooter} from "reactstrap";�                 &import React, {useState} from "react";5�_�                    )       ����                                                                                                                                                                                                                                                                                                                                                             _6�     �   (   *   ;                <Reply />5�_�                    /       ����                                                                                                                                                                                                                                                                                                                                                             _7�    �   .   0   ;                  form="createthread"5�_�                    /       ����                                                                                                                                                                                                                                                                                                                                                             _7�   	 �   6                      </ModalFooter>         </Modal>   
    </div>     );   };�   5   7                    </Button>�   4   6                      Cancel�   3   5          5          <Button color="secondary" onClick={toggle}>�   2   4                    </Button>{" "}�   1   3                      Submit�   0   2                    >�   /   1                      onClick={toggle}�   .   0                      form="reply"�   -   /                      type="submit"�   ,   .                      color="primary"�   +   -                    <Button�   *   ,                  <ModalFooter>�   )   +                  </ModalBody>�   (   *          3          <Reply indexLastReply={indexLastReply} />�   '   )                  <ModalBody>�   &   (                  </ModalHeader>�   %   '                    reply�   $   &          6        <ModalHeader toggle={toggle} close={closeBtn}>�   #   %                >�   "   $          #        external={externalCloseBtn}�   !   #                  className={className}�       "                  toggle={toggle}�      !                  isOpen={modal}�                       <Modal�                5      <Button onClick={toggle}>{buttonLabel}</Button>�                     <div className="replymodal">�                
  return (�                  );�                    </button>�                      &times;�                /    <button className="close" onClick={toggle}>�                  const closeBtn = (�                  );�                    </button>�                      &times;�                    >�                      onClick={toggle}�                @      style={{position: "absolute", top: "15px", right: "15px"}}�                      className="close"�                    <button�                  const externalCloseBtn = (�                 �                (  const toggle = () => setModal(!modal);�   
              �   	             ,  const [modal, setModal] = useState(false);�      
           �      	          9  const {buttonLabel, className, indexLastReply} = props;�                &export const ReplyModal = (props) => {�                 �                import {Reply} from "./reply";�                import "./reply_modal.css";�                 �                Nimport {Button, Modal, ModalHeader, ModalBody, ModalFooter} from "reactstrap";�                 &import React, {useState} from "react";5�_�                    )   /    ����                                                                                                                                                                                                                                                                                                                                                             _��   
 �   (   *   6      3          <Reply indexLastReply={indexLastReply} />5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _��    �   5   7          };�   4   6            );�   3   5          
    </div>�   2   4                </Modal>�   1   3                  </ModalFooter>�   0   2                    </Button>�   /   1                      Cancel�   .   0          5          <Button color="secondary" onClick={toggle}>�   -   /                    </Button>{" "}�   ,   .                      Submit�   +   -          N          <Button color="primary" type="submit" form="reply" onClick={toggle}>�   *   ,                  <ModalFooter>�   )   +                  </ModalBody>�   (   *          0          <Reply indexLastReply={indexThread} />�   '   )                  <ModalBody>�   &   (                  </ModalHeader>�   %   '                    reply�   $   &          6        <ModalHeader toggle={toggle} close={closeBtn}>�   #   %                >�   "   $          #        external={externalCloseBtn}�   !   #                  className={className}�       "                  toggle={toggle}�      !                  isOpen={modal}�                       <Modal�                5      <Button onClick={toggle}>{buttonLabel}</Button>�                     <div className="replymodal">�                
  return (�                  );�                    </button>�                      &times;�                /    <button className="close" onClick={toggle}>�                  const closeBtn = (�                  );�                    </button>�                      &times;�                    >�                      onClick={toggle}�                @      style={{position: "absolute", top: "15px", right: "15px"}}�                      className="close"�                    <button�                  const externalCloseBtn = (�                 �                (  const toggle = () => setModal(!modal);�   
              �   	             ,  const [modal, setModal] = useState(false);�      
           �      	          9  const {buttonLabel, className, indexLastReply} = props;�                &export const ReplyModal = (props) => {�                 �                import {Reply} from "./reply";�                import "./reply_modal.css";�                 �                Nimport {Button, Modal, ModalHeader, ModalBody, ModalFooter} from "reactstrap";�                 &import React, {useState} from "react";5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             _�     �      	   6      ;  const { buttonLabel, className, indexLastReply } = props;5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                             _�    �      	   6      6  const { buttonLabel, className, indexLast } = props;5�_�                     )       ����                                                                                                                                                                                                                                                                                                                                                             _է    �   (   *   6      0          <Reply indexLastReply={indexThread} />5��