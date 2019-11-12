<template>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12 main-bar">
          <h4>VIEW AUDIO SET {{audioName}}</h4>
        </div>
        </div>

        <div class="row">
            <div class="col-lg-12"  style="margin-bottom: 20px;">

  <v-card
    class="mx-auto"
    max-width="642"
  >
    		<youtube :video-id="videoId" />

    <p class="pb-0"></p>

    <v-card-text class="text--primary">
            <div><strong>Name: </strong> {{audioName ? audioName : 'N/A'}}</div>

      <div>
        <v-textarea v-if="audioTranscribed === 'false' || id === audioAnnotator"
  class="purple-input"
  label="Transcription"
  :value="audioTranscription"
        v-model="audioTranscription"/>
        <p v-else>Transcribed: True</p>
      </div>

      <div><strong>Details: </strong> {{audioDetails ? audioDetails : 'N/A'}}</div>
      <div><strong>Tags: </strong> {{audioTags ? audioTags : 'N/A'}}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn v-if="audioTranscribed === 'false' || id === audioAnnotator"
        color="green"
        text
        v-on:click="saveTranscription()"
      >
        Save
      </v-btn>
    </v-card-actions>
  </v-card>
            </div>
        </div>
      <br>
    </div>
</template>

<script>
    import axios from 'axios';
import VueTagsInput from '@johmun/vue-tags-input';

    export default {
        name: "ViewAudioSet",
        data: () => ({
            audioID: localStorage.getItem('audioID'),
            audioName: localStorage.getItem('audioName'),
            audioDetails: localStorage.getItem('audioDetails'),
            audioTranscribed: localStorage.getItem('audioTranscribed'),
            audioTranscription: localStorage.getItem('audioTranscription'),
            audioAnnotator: localStorage.getItem('audioAnnotator'),
            audioTags: localStorage.getItem('audioTags'),
            audioUrl: localStorage.getItem('audioUrl'),
            videoId: localStorage.getItem('videoId'),
            id: localStorage.getItem('id'),
        }),
        methods: {
          saveTranscription: function () {
                    axios.put('http://localhost:8080/api/Audios/'+this.audioID+"/",
                        {
                            "id" : this.audioID,
                            "name": this.audioName,
                            "annotator" :this.id,
                            "transcription": this.audioTranscription,
                            "transcribed" : true,
                            "details" : this.audioDetails,
                            "tags" : this.audioTags,
                            "url" : this.audioUrl
                        },
                        {
                            headers: {
                                'Authorization': 'token '+ localStorage.getItem('token'),
                                'Access-Control-Allow-Origin' : '*'
                            }
                        }
                    ).then((res) => {
                        if (res.request.status === 200) {
                    this.$swal({type: 'success', title: 'Thank you', text: 'Transcription has been added successfully!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                        } else {
                    this.$swal({type: 'warning', title: 'Something Wrong Happened', text: 'Please check the info and try again!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                        }
                    }).catch((err) => {
                      if (err) {
                        throw err;
                      }
                    });
          }
        },
        mounted() {
        },

    }
</script>
<style lang="css">
    @font-face {
  font-family: 'industry';
  src:  url('../styles/fonts/Industry-Bold.woff') format('woff'),
        url('../styles/fonts/Industry-Bold.eot') format('eot');
  font-weight: bold;
  font-style: normal;
}

    .main-bar {
        height: 60px;
        background-color: #0d47a1;
        color: white;
        text-align: center;
        padding: auto;
        margin-bottom: 30px;
    }
    h4{
        font-family: "industry",sans-serif !important;
        padding-top: 0.5%;
    }
</style>