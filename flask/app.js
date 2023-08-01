const {
  createApp
} = Vue
createApp({
data(){
  return{
    weight:"",
    height:"",
    bmi:"",
    result:""
  }
},
created(){
  console.log("hello")
},
methods:{
  culcBmi(){
    this.bmi = this.weight / ((this.height * 0.01)**2);
    this.judge()
  }
}
}).mount("#app")

createApp({
  data() {
    return {
      msg:" ",
    }
  },
  created() {
    axios.get('http://localhost:8080/supplyments').then(res => {
      let arr = res.data.supplyments
      this.catalogs = arr
      console.log(this.catalogs)
    });
  },
  computed: {
    hoge(){
      console.log(this.msg)
    }
  }
}).mount('#app')