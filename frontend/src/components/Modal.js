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

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeVehiculo: this.props.activeVehiculo,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeVehiculo = { ...this.state.activeVehiculo, [name]: value };

    this.setState({ activeVehiculo });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Vehiculo</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="todo-title">Nombre</Label>
              <Input
                type="text"
                id="todo-title"
                name="Nombre"
                value={this.state.activeVehiculo.Nombre}
                onChange={this.handleChange}
                placeholder="Vehiculo nombre"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Ubicacion actual latitud</Label>
              <Input
                type="text"
                id="todo-description"
                name="Ubicacion_actual_lat"
                value={this.state.activeVehiculo.Ubicacion_actual_lat}
                onChange={this.handleChange}
                placeholder="Latitud ubicacion actual"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Ubicacion actual longitud</Label>
              <Input
                type="text"
                id="todo-description"
                name="Ubicacion_actual_long"
                value={this.state.activeVehiculo.Ubicacion_actual_long}
                onChange={this.handleChange}
                placeholder="Longitud ubicacion actual"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Consumo combustible</Label>
              <Input
                type="text"
                id="todo-description"
                name="Consumo_combustible"
                value={this.state.activeVehiculo.Consumo_combustible}
                onChange={this.handleChange}
                placeholder="Enter consumo combustible promedio"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Distancia recorrida</Label>
              <Input
                type="text"
                id="todo-description"
                name="Distancia_recorrida"
                value={this.state.activeVehiculo.Distancia_recorrida}
                onChange={this.handleChange}
                placeholder="Enter distancia recorrida"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Combustible consumido</Label>
              <Input
                type="text"
                id="todo-description"
                name="Combustible_consumido"
                value={this.state.activeVehiculo.Combustible_consumido}
                onChange={this.handleChange}
                placeholder="Enter combustible utlizado"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeVehiculo)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}