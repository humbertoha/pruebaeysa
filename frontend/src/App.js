import React, { useEffect, useState,Component } from "react";
import {Tab,Tabs,TabList,TabPanel} from 'react-tabs';
import 'react-tabs/style/react-tabs.css';

import Modal from "./components/Modal";
import Modaldos from "./components/Modaldos";
import axios from "axios";
import Select from "react-select";
import { Label } from "reactstrap";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      vehiculoList: [],
      RutaList: [],
      EstadoList: [],
      estado:"",
      modal: false,
      activeVehiculo: {
        id: "",
        Nombre: "",
        Ubicacion_actual_lat:"",
        Ubicacion_actual_long : "",
        Consumo_combustible : "",
        Distancia_recorrida : "",
        Combustible_consumido : ""
      },
      modalruta: false,
      activeRuta: {
        id: "",
        Nombre: "",
        Estatus:"",
        paradas : []
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/Vehiculos/")
      .then((res) => this.setState({ vehiculoList: res.data }))
      .catch((err) => console.log(err));
    axios
      .get("/api/Ruta/")
      .then((res) => this.setState({ RutaList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });   
  };

  toggleruta = () => {
    this.setState({ modalruta: !this.state.modalruta });   
  };

  handleSubmit = (Vehiculo) => {
    this.toggle();

    if (Vehiculo.id) {
      axios
        .put(`/api/Vehiculos/${Vehiculo.id}/`, Vehiculo)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/api/Vehiculos/", Vehiculo)
      .then((res) => this.refreshList());
  };

  handleSubmitRuta = (Ruta) => {
    console.log(Ruta);
    this.toggleruta();

    if (Ruta.id) {
      axios
        .put(`/api/Ruta/${Ruta.id}/`, Ruta)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/api/Ruta/", Ruta)
      .then((res) => this.refreshList());
  };

  handleDelete = (Vehiculo) => {
     axios
      .delete(`/api/Vehiculos/${Vehiculo.id}/`)
      .then((res) => this.refreshList());
  };

  handleDeleteRuta = (Ruta) => {
     axios
      .delete(`/api/Ruta/${Ruta.id}/`)
      .then((res) => this.refreshList());
  };
 
  handleRutavehiculo = (e,Vehiculo)=>{
    const rutavehiculo = {
      id_vehiculos : Vehiculo.id,
      id_ruta : this.state.RutaList.find((element)=> { return element.id === e.value } ).id
    };
    axios
      .post("/api/RutaVehiculo/", rutavehiculo)
      .then((res) => this.refreshList());
  };
  createVehiculo = () => {
    const vehiculo = { 
        id: "",
        Nombre: "",
        Ubicacion_actual_lat:"",
        Ubicacion_actual_long : "",
        Consumo_combustible : "",
        Distancia_recorrida : "",
        Combustible_consumido : "",
        completed: false 
      };

    this.setState({ activeVehiculo: vehiculo, modal: !this.state.modal });
  };

  createRuta = () => {
    const ruta = { 
        id: "",
        Nombre: "",
        Estatus:"",
        paradas:[]
      };

    this.setState({ activeRuta: ruta, modalruta: !this.state.modalruta });
  };
  editVehiculo = (Vehiculo) => {
    this.setState({ activeVehiculo: Vehiculo, modal: !this.state.modal });
  };

  editRuta = (Ruta) => {
    this.setState({ activeRuta: Ruta, modalruta: !this.state.modalruta });
  };

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }

    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
       
      <TabList>
        <Tab>Vehiculos</Tab>
        <Tab>Ruta</Tab>
      </TabList>
    );
  };

  renderVehiculos = () => {
    return this.state.vehiculoList.map((Vehiculo) => (
      <li
        key={Vehiculo.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2`}
        >
          {Vehiculo.Nombre}
        </span>
        <span
          className={`todo-title mr-2`}
        >
          { Object.keys(Vehiculo.ruta).length>0  ? Vehiculo.ruta[0].id_ruta.Nombre : "" }
        </span>
        <span>
              <Select
                name="RutaVehiculo"
                placeholder="Selecciona una ruta"
                searchable={false}
                onChange= {(e) =>this.handleRutavehiculo(e,Vehiculo)}
                options= {this.state.RutaList.map(e => ({ label: e.Nombre, value: e.id}))}
              />
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editVehiculo(Vehiculo)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(Vehiculo)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  renderRuta = () => {
    return this.state.RutaList.map((Ruta) => (
      <li
        key={Ruta.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2`}
        >
          {Ruta.Nombre}
        </span>
        <span
          className={`todo-title mr-2`}
        >
          {Ruta.Estatus}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editRuta(Ruta)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDeleteRuta(Ruta)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-12">Producto ejemplo</h1>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
              <span>
                <button
                  className="btn btn-primary"
                  onClick={this.createVehiculo}
                >
                  Vehiculo nuevo 
                </button>
              </span>
              <span>
                 <button
                  className="btn btn-primary"
                  onClick={this.createRuta}
                >
                  Ruta nuevo 
                </button>
                </span>
              </div>
              <Tabs className="mb-3" >
                {this.renderTabList()}
              <TabPanel>
              <ul className="list-group list-group-flush border-top-0">
                <li class="list-group-item d-flex justify-content-between align-items-center" >
                  <span class="todo-title mr-2">Nombre vehiculo</span>
                  <span class="todo-title mr-2">Nombre de ruta asignada</span>
                  <span class="todo-title mr-2">Asignar Ruta</span>
                  <span class="todo-title mr-2">Acciones</span>
                  <span></span>
                </li>
                {this.renderVehiculos()}
              </ul>
              </TabPanel>
              <TabPanel>
              <ul className="list-group list-group-flush border-top-0">
                <li class="list-group-item d-flex justify-content-between align-items-center" >
                  <span class="todo-title mr-2">Nombre ruta</span>
                </li>
                {this.renderRuta()}
              </ul>
              </TabPanel>
              </Tabs>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeVehiculo={this.state.activeVehiculo}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
        {this.state.modalruta ? (
          <Modaldos
            activeRuta={this.state.activeRuta}
            toggle={this.toggleruta}
            onSave={this.handleSubmitRuta}
          />
        ) : null}
      </main>
    );
  }
}

export default App;