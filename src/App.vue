<template>
  <v-app>
  <div v-if="welcome">

    <!--<v-btn @click="welcome=false">Click this ho </v-btn>-->

  </div>

  <div v-else-if="!welcome">
    <v-toolbar> hello </v-toolbar>
     <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex xs12>
                  <p>hello</p>
                  {{info}}
                </v-flex>
                <v-flex xs6>
                    <v-card>
                      <!--RESUME UPLOAD BEGINS-->
                      <div v-for="item in items">
                          <div v-if="!item.image">
                            <v-layout column wrap align-center>
                              <v-flex x12 sm3>
                                  <h2>Upload Your Resume Here</h2>
                              </v-flex>
                              <v-flex x12 sm3>
                                  <p>hello</p>
                              </v-flex>
                              <v-flex x12 sm3>
                                  <div class="file-upload">
                                  <div class="file-select">
                                      <input type="file" name="chooseFile" id="chooseFile" accept=".docx" @change="onFileChange($event)">
                                  </div>
                                  </div>
                              </v-flex>
                            </v-layout>
                          </div>

                          <div v-else>
                            <v-layout column>
                                <v-flex x12 sm3>
                                <img id="displayedPic" :src="item.image" />
                                </v-flex>
                                <v-flex x12 sm3>
                                <v-btn color="primary" @click="removeImage(item),emitGlobalClickEvent()">Choose Another Image</v-btn>
                                </v-flex>
                            </v-layout>
                          </div>
                      </div>
                      <!--RESUME UPLOAD ENDS-->
                    </v-card>
                </v-flex xs6>

                <v-flex xs6>
                    <v-card>

                    </v-card>
                </v-flex xs6>
            </v-layout>
        </v-container>
    </div>
  </v-app>
</template>

<script>
import { upload } from './file-upload.service';
import * as axios from 'axios';

export default {
    name: 'app',
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'photos',
        items: [
         {
           image: false,
         },
        ],
        welcome: false,
        info:null,
      }
    },
    computed: {
    },
    methods: {
    reset(){

    },
    onFileChange(event){
        let data = new FormData();
        let file = event.target.files[0];

        data.append('name', 'my-file')
        data.append('file', file)
        let config = {
          header : {
           'Content-Type' : 'multipart/form-data'
         }
        }
        upload(data)

    }
    },

};

</script>

<style>

</style>
