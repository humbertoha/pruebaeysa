import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";
import Select from "react-select";
import axios from "axios";


export default class CustomModal extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      activeRuta: this.props.activeRuta,
      EstadoList : [],
      MunicipioList : [],
      LocalidadList : [],
      RutaList : this.props.RutaList,
      municipio : "",
      estado: "",
      localidad : ""
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeRuta = { ...this.state.activeRuta, [name]: value };

    this.setState({ activeRuta });
  };

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/Estado/")
      .then((res) => this.setState({ EstadoList: res.data }))
      .catch((err) => console.log(err));
  };

  MunicipioOptions = () => {
    console.log("Estado "+this.state.estado.value)
    if (this.state.estado.value>0) {
      return axios
      .get("/api/Municipio/?Id_estado="+this.state.estado.value)
      .then((res) => this.setState({ MunicipioList: res.data }))
      .catch((err) => console.log(err));
        
    } else {
      return "";
    }
  };

  LocalidadOptions = () => {
    console.log("Estado "+this.state.municipio.value)
    if (this.state.municipio.value>0) {
      return axios
      .get("/api/Localidad/?Id_municipio="+this.state.municipio.value+"&Id_estado="+this.state.estado.value)
      .then((res) => this.setState({ LocalidadList: res.data }))
      .catch((err) => console.log(err));
        
    } else {
      return "";
    }
  };

  handleEstados = (e) => {
     this.setState({ estado : e},() => {this.MunicipioOptions();});
     //;
     this.setState({ municipio : null});
  };

  handleMunicipio = (e) => {
     this.setState({ municipio : e },() => {this.LocalidadOptions();});
     //this.LocalidadOptions();
     this.setState({ localidad : null});
  };

  handleLocalidad = (e) => {
    let { activeRuta } = this.state;
    let localidaddata = this.state.LocalidadList.find((element)=> { return element.id === e.value } );
    console.log(localidaddata);
    this.setState({ localidad : e },() => { activeRuta.paradas.push({ id:"",Id_localidad: localidaddata});this.setState( { activeRuta:activeRuta } )});
    console.log(this.state.activeRuta);
     //this.LocalidadOptions();
     //this.setState({ localidad : null});
  };

  handleDeleteParada = (Parada) =>{
     if(Parada.id!=""){
       axios
        .delete(`/api/Paradas/${Parada.id}/`);
       let { activeRuta } = this.state;
       activeRuta.paradas =  activeRuta.paradas.filter(element => element.id !== Parada.id )
       this.setState({activeRuta}); 
    }else{
       let { activeRuta } = this.state;
       activeRuta.paradas =  activeRuta.paradas.filter(element => element.Id_localidad.id !== Parada.Id_localidad.id )
       this.setState({activeRuta}); 
    }
  };

   renderParadas = () => {
    return this.state.activeRuta.paradas.map((parada) => (
      <li
        key={parada.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2`}
        >
          {parada.Id_localidad.Nombre}
        </span>
        <span>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDeleteParada(parada)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Ruta</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="todo-title">Ruta nombre</Label>
              <Input
                type="text"
                id="todo-title"
                name="Nombre"
                value={this.state.activeRuta.Nombre}
                onChange={this.handleChange}
                placeholder="Enter Vehiculo nombre"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Estatus</Label>
              <Input
                type="checkbox"
                id="todo-description"
                name="Estatus"
                value={this.state.activeRuta.Estatus}
                onChange={this.handleChange}
                placeholder="Enter producto description"
              />
            </FormGroup>
         
          <h2> Agregar Parada</h2>
              <FormGroup>
              <Label for="todo-description">Estado</Label>
              <Select
                id="Estado"
                name= "estado"
                placeholder="Select a brand"
                searchable={false}
                value = {this.state.estado} 
                onChange= {this.handleEstados}
                options={this.state.EstadoList.map(e => ({ label: e.Nombre, value: e.id}))}
                />
              </FormGroup>
              <FormGroup>
              <Label for="todo-description">Municipio</Label>
              <Select
                id="Municipio"
                name="municipio"
                placeholder="Select a brand"
                searchable={false}
                value = {this.state.municipio}
                onChange= {this.handleMunicipio}
                options= {this.state.MunicipioList.map(e => ({ label: e.Nombre, value: e.id}))}
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Localidad</Label>
              <Select
                id="Localidad"
                name="Id_localidad"
                placeholder="Select a brand"
                searchable={false}
                value = {this.state.localidad}
                onChange= {this.handleLocalidad}
                options= {this.state.LocalidadList.map(e => ({ label: e.Nombre, value: e.id}))}
              />
            </FormGroup>
           </Form>
           <div>
           {this.renderParadas()}
           </div>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeRuta)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}