<template>
  <v-app>
  <div v-if="welcome">

    <!--<v-btn @click="welcome=false">Click this ho </v-btn>-->
    <my-button type="Click here to push Meera's buttons" @click="toggleLable">{{label}}</my-button>


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
const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;

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
<<<<<<< HEAD
        welcome: true,
=======
        welcome: false,
        info:null,
>>>>>>> 33dea6fdab013b6cfba5ce87b8a8946e8b560421
      }
    },
    computed: {
      isInitial() {
        return this.currentStatus === STATUS_INITIAL;
      },
      isSaving() {
        return this.currentStatus === STATUS_SAVING;
      },
      isSuccess() {
        return this.currentStatus === STATUS_SUCCESS;
      },
      isFailed() {
        return this.currentStatus === STATUS_FAILED;
      }
    },
    methods: {
      toggleLable: function(e) {
      console.log(e.target.tagName);
      if (this.label == "Click here to push Meera's buttons") {
        this.label = "Meera's buttons are pushed, oh boi";
      } else {
        this.label = "Click here to push Meera's buttons";
      }
      //console.log(this.label);
    },
      reset() {
        // reset form to initial state
        this.currentStatus = STATUS_INITIAL;
        this.uploadedFiles = [];
        this.uploadError = null;
      },
      save(formData) {
        // upload data to the server
        this.currentStatus = STATUS_SAVING;

        upload(formData)
          .then(x => {
            this.uploadedFiles = [].concat(x);
            this.currentStatus = STATUS_SUCCESS;
          })
          .catch(err => {
            this.uploadError = err.response;
            this.currentStatus = STATUS_FAILED;
          });
      },
      filesChange(fieldName, fileList) {
        // handle file changes
        const formData = new FormData();

        if (!fileList.length) return;

        // append the files to FormData
        Array
          .from(Array(fileList.length).keys())
          .map(x => {
            formData.append(fieldName, fileList[x], fileList[x].name);
          });

        // save it
        this.save(formData);
    },
    onFileChange(event){
        /*let data = new FormData();
        let file = event.target.files[0];

        data.append('name', 'my-file')
        data.append('file', file)
        let config = {
          header : {
           'Content-Type' : 'multipart/form-data'
         }
        }
        upload(data)*/

    }
    },
    mounted() {
      this.reset();
      axios
          .post('/127.0.0.1:5000/uploads/data')
          .then(response => (this.info = response))
    }

};

</script>

<style>

</style>
