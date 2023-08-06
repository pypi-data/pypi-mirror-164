from .Layer import Layer
import numpy as np


class NN:


    def __init__(self, layers, learning_rate):
        self.learning_rate = learning_rate
        self.layers = []
        temp_layer = 0
        for layer in range(len(layers)):
            self.add_layer(inputs=layers[temp_layer][0], 
                           neurons=layers[layer][0], 
                           activation_function=layers[layer][1], 
                           last_layer=True if layer == len(layers) - 1 else False,
                           first_layer=True if temp_layer == 0 else False,
                           id=layer)
            temp_layer = layer

    def add_layer(self, inputs, neurons, activation_function, last_layer, first_layer, id):
        self.layers.append(Layer(inputs, 
                                 neurons, 
                                 activation_function, 
                                 last_layer, 
                                 first_layer, 
                                 id))

    def predict(self, num_of_train):
        input_for_next_layer = self.full_data_input[num_of_train]
        for layer_num in range(len(self.layers)):
            input_for_next_layer = self.layers[layer_num].forward_propagation(input_for_next_layer)
        return np.argmax(input_for_next_layer)

    def full_backward_pass(self, num_of_training):
        number_of_layers = len(self.layers) - 1 if len(self.layers) - 1 != 0 else len(self.layers)
        for layer_num in range(number_of_layers, -1, -1):
            prev_layer = self.layers[layer_num - 1] if layer_num - 1 >= 0 else None
            next_layer = self.layers[layer_num + 1] if layer_num + 1 < len(self.layers) else None
            self.layers[layer_num].back_propagation(self.full_data_output[num_of_training],
                                                    self.full_data_input[num_of_training], 
                                                    prev_layer, 
                                                    next_layer)

    def load_data_with_output(self, data):
        self.full_data_input = []
        self.full_data_output = []
        max_number_in_input_data = np.amax(np.abs(np.array(data)))
        for i in data:
            self.full_data_input.append(np.array(i)[1:] / max_number_in_input_data)
            self.full_data_output.append(self.create_output(i[0], 
                                         len(i) - 1))

    @staticmethod
    def create_output(etiquette, number_of_possible_outputs):
        data_output = []
        for i in range(0, number_of_possible_outputs):
            data_output.append(1 if i == etiquette else 0)
        return data_output

    def load_data(self, data):
        self.full_data_input = []
        max_number_in_input_data = np.amax(np.abs(np.array(data)))
        for i in data:
            self.full_data_input.append(np.array(i) / max_number_in_input_data)

    def learn(self, max_epoch_number):
        accuracy, prev_accuracy = 0, 0
        for i in range(max_epoch_number):
            temp = 0
            for j in range(0, len(self.full_data_input)):
                prediction = self.predict(j)
                temp += self.check_if_same_result(prediction, np.argmax(self.full_data_output[j]))
                self.full_backward_pass(j)
                self.update_all()
            break_flag, prev_accuracy = self.calculate_accuracy(temp, prev_accuracy, accuracy, i)
            if break_flag: break

    @staticmethod
    def check_if_same_result(prediction, etiquette):
        return 1 if prediction == etiquette else 0

    def calculate_accuracy(self, temp, prev_accuracy, accuracy, epoch):
        accuracy = temp/len(self.full_data_input)
        if accuracy == prev_accuracy and accuracy > 0.999:
            return True, accuracy
        print("Accuracy: " + str(temp/len(self.full_data_input)) + " | Epoch: " + str(epoch + 1))
        return False, accuracy

    def update_all(self):
        for layer_num in range(0, len(self.layers) - 1):
            self.layers[layer_num].update_values(self.learning_rate)

    def save_variables(self):
        for layer in self.layers:
            layer.save_to_file()

    def load_variables(self):
        for layer in self.layers:
            layer.load_from_file()
