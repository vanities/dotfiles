Vim�UnDo� ,b G4<凹��6N��N�+��B���v��w   �   M        videoDocId = await videosCollection.createDocument({ some: "data" });       I      	       	   	   	    _>��    _�                     V   .    ����                                                                                                                                                                                                                                                                                                                                                             _=Y�     �   U   W   �      3                        "admirerThumbnailImageUrl",5�_�                    V        ����                                                                                                                                                                                                                                                                                                                                                             _=Y�    �   U   W   �      <                        "admirerThumbnailImageThumbnailUrl",5�_�                        I    ����                                                                                                                                                                                                                                                                                                                                                             _>��     �      !   �      M        videoDocId = await videosCollection.createDocument({ some: "data" });5�_�                        Y    ����                                                                                                                                                                                                                                                                                                                                                             _>��    �      !   �      ^      videoDocId = await videosCollection.createDocument({ some: "data", { funMetadata: {} });5�_�                        z    ����                                                                                                                                                                                                                                                                                                                                                             _>��     �      !   �      |      videoDocId = await videosCollection.createDocument({ some: "data", { funMetadata: { imageThumbnailUrl: "some-url"} });5�_�                        x    ����                                                                                                                                                                                                                                                                                                                                                             _>��     �      !   �      |      videoDocId = await videosCollection.createDocument({ some: "data", { funMetadata: { imageThumbnailUrl: "some-url"} });5�_�                        K    ����                                                                                                                                                                                                                                                                                                                                                             _>��     �      !   �      }      videoDocId = await videosCollection.createDocument({ some: "data", { funMetadata: { imageThumbnailUrl: "some-url"}} });5�_�      	                  y    ����                                                                                                                                                                                                                                                                                                                                                             _>��    �      !   �      {      videoDocId = await videosCollection.createDocument({ some: "data", funMetadata: { imageThumbnailUrl: "some-url"}} });5�_�                  	       w    ����                                                                                                                                                                                                                                                                                                                                                             _>��    �   �            �   �   �          });�   �   �              });�   �   �                  });�   �   �                      });�   �   �                          );�   �   �                              }�   �   �          ?                        message: "Error: Couldn't find video.",�   �   �          &                        name: "Error",�   �   �                              {�   �   �                              }),�   �   �          .                        videoId: "missing-id",�   �   �          0                        message: "some-message",�   �   �          0                        receiverUid: "some-uid",�   �   �          .                        senderUid: "some-uid",�   �   �          :                    test.wrap(functions.addFunWheelLike)({�   �   �          %                await assert.rejects(�   �   �          T            it("should throw error when videoId is not in collection", async () => {�   �   �           �   �   �                      });�   �   �                          ]);�   �   �                              ),�   �   �          %                        errorResponse�   �   �                                  }),�   �   �          (                            videoId: "",�   �   �          4                            message: "some-message",�   �   �          4                            receiverUid: "some-uid",�   �   �          2                            senderUid: "some-uid",�   �   �          >                        test.wrap(functions.addFunWheelLike)({�      �          #                    assert.rejects(�   ~   �           �   }                                 ),�   |   ~          %                        errorResponse�   {   }                                  }),�   z   |          (                            message: "",�   y   {          4                            receiverUid: "some-uid",�   x   z          2                            senderUid: "some-uid",�   w   y          >                        test.wrap(functions.addFunWheelLike)({�   v   x          #                    assert.rejects(�   u   w           �   t   v                              ),�   s   u          %                        errorResponse�   r   t                                  }),�   q   s          ,                            receiverUid: "",�   p   r          2                            senderUid: "some-uid",�   o   q          >                        test.wrap(functions.addFunWheelLike)({�   n   p          #                    assert.rejects(�   m   o           �   l   n                              ),�   k   m          %                        errorResponse�   j   l          P                        test.wrap(functions.addFunWheelLike)({ senderUid: "" }),�   i   k          #                    assert.rejects(�   h   j           �   g   i                              ),�   f   h          %                        errorResponse�   e   g          A                        test.wrap(functions.addFunWheelLike)({}),�   d   f          #                    assert.rejects(�   c   e          #                await Promise.all([�   b   d           �   a   c                          };�   `   b          6                    message: "Request missing value.",�   _   a          "                    name: "Error",�   ^   `          '                const errorResponse = {�   ]   _          M            it("should throw error when missing required data", async () => {�   \   ^          .        describe("invalid data", function () {�   [   ]           �   Z   \                  });�   Y   [                      });�   X   Z                          );�   W   Y                              )�   V   X          F                        admirerVideoData.funMetadata.imageThumbnailUrl�   U   W          3                        "admirerImageThumbnailUrl",�   T   V          -                        likesCollection.name,�   S   U          =                    await helpers.document_with_field_exists(�   R   T                          assert.ok(�   Q   S          J                // we only check imageThumbnailUrl for tests to be concise�   P   R                          );�   O   Q                              )�   N   P          &                        data.senderUid�   M   O          %                        "admirerUid",�   L   N          -                        likesCollection.name,�   K   M          =                    await helpers.document_with_field_exists(�   J   L                          assert.ok(�   I   K          0                assert.equal("success", result);�   H   J          P                const result = await test.wrap(functions.addFunWheelLike)(data);�   G   I                          };�   F   H          1                    message: "fun wheel message",�   E   G          5                    receiverUid: "some-receiver-uid",�   D   F          )                    senderUid: senderUid,�   C   E          (                    videoId: videoDocId,�   B   D                          data = {�   A   C                          // add like�   @   B           �   ?   A          H                await videosCollection.createDocument(admirerVideoData);�   >   @                          };�   =   ?                              },�   <   >          +                        userUid: senderUid,�   ;   =          <                        videoThumbnailUrl: "some-video-url",�   :   <          3                        videoUrl: "some-video-url",�   9   ;          <                        imageThumbnailUrl: "some-image-url",�   8   :          3                        imageUrl: "some-image-url",�   7   9          "                    funMetadata: {�   6   8          *                const admirerVideoData = {�   5   7          $                // add admirer video�   4   6           �   3   5          A                const senderUid = `some-sender-uid-${shortUuid}`;�   2   4          Q            it("should create a like document with correct values", async () => {�   1   3          ,        describe("valid data", function () {�   0   2          -    describe("addFunWheelLike", function () {�   /   1           �   .   0              });�   -   /                  ]);�   ,   .          >            videosFullStorage.deleteFile(remoteVideoFilename),�   +   -          R            helpers.deleteCollection(admin.firestore(), videosCollection.name, 1),�   *   ,          Q            helpers.deleteCollection(admin.firestore(), likesCollection.name, 1),�   )   +                  await Promise.all([�   (   *              after(async () => {�   '   )           �   &   (              });�   %   '          &        await uploadTikTok(shareLink);�   $   &          3        shareLink = "https://vm.tiktok.com/3awDGF";�   #   %          8        remoteVideoFilename = "6792361683743526150.mp4";�   "   $          .        // changing these will prevent cleanup�   !   #          ?        // shareLink embeds the videoId in remoteVideoFilename,�       "           �      !          z      videoDocId = await videosCollection.createDocument({ some: "data", funMetadata: { imageThumbnailUrl: "some-url"}} );�                  �                J        videosCollection.name = `${collectionPrefix}-videos-${shortUuid}`;�                H        likesCollection.name = `${collectionPrefix}-likes-${shortUuid}`;�                0        shortUuid = `${uuid()}`.substring(0, 7);�                0        collectionPrefix = "add_fun_wheel_like";�                1    // set unique collection name for these tests�                    before(async () => {�                 �                    let videoDocId;�                    let shortUuid;�                    let collectionPrefix;�                    let shareLink;�                    let remoteVideoFilename;�                    let data;�                    this.timeout(100000);�                ,describe("add_fun_wheel_like", function () {�                 �                    .videosFullStorage;�                Bconst videosFullStorage = require("../lib/utils/cloud_storage.js")�                    .videosCollection;�   
             Econst videosCollection = require("../lib/utils/firestore_collection")�   	                 .likesCollection;�      
          Dconst likesCollection = require("../lib/utils/firestore_collection")�      	          Lconst uploadTikTok = require("../lib/utils/tiktok_scraper.js").uploadTikTok;�                Jconst functions = require("../lib/http/tasks/on_call/add_fun_wheel_like");�                %const helpers = require("./helpers");�                 �                1const { admin, test } = require("./test_config");�                 �                %const { v4: uuid } = require("uuid");�                 !const assert = require("assert");5��