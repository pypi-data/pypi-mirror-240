import tensorflow as tf

from pidgan.players.discriminators.Discriminator import Discriminator


class AuxDiscriminator(Discriminator):
    def __init__(
        self,
        output_dim,
        aux_features,
        num_hidden_layers=5,
        mlp_hidden_units=128,
        mlp_dropout_rates=0,
        output_activation="sigmoid",
        name=None,
        dtype=None,
    ) -> None:
        super().__init__(
            output_dim=output_dim,
            num_hidden_layers=num_hidden_layers,
            mlp_hidden_units=mlp_hidden_units,
            mlp_dropout_rates=mlp_dropout_rates,
            output_activation=output_activation,
            name=name,
            dtype=dtype,
        )

        self._aux_features = list()
        if isinstance(aux_features, str):
            aux_features = [aux_features]

        self._aux_indices = list()
        self._aux_operators = list()
        for aux_feat in aux_features:
            assert isinstance(aux_feat, str)
            if "+" in aux_feat:
                self._aux_operators.append(tf.math.add)
                self._aux_indices.append([int(i) for i in aux_feat.split("+")])
            elif "-" in aux_feat:
                self._aux_operators.append(tf.math.subtract)
                self._aux_indices.append([int(i) for i in aux_feat.split("-")])
            elif "*" in aux_feat:
                self._aux_operators.append(tf.math.multiply)
                self._aux_indices.append([int(i) for i in aux_feat.split("*")])
            elif "/" in aux_feat:
                self._aux_operators.append(tf.math.divide)
                self._aux_indices.append([int(i) for i in aux_feat.split("/")])
            else:
                raise ValueError(
                    f"Operator for auxiliary features not supported. "
                    f"Operators should be selected in ['+', '-', '*', '/'], "
                    f"instead '{aux_feat}' passed."
                )
            self._aux_features.append(aux_feat)

    def _prepare_input(self, inputs) -> tf.Tensor:
        std_input_feats = tf.concat(inputs, axis=-1)
        _, y = inputs
        aux_input_feats = list()
        for aux_idx, aux_op in zip(self._aux_indices, self._aux_operators):
            aux_input_feats.append(aux_op(y[:, aux_idx[0]], y[:, aux_idx[1]])[:, None])
        self._aux_input_feats = tf.concat(aux_input_feats, axis=-1)
        return tf.concat([std_input_feats, self._aux_input_feats], axis=-1)

    def call(self, inputs, return_aux_features=False) -> tf.Tensor:
        out = super().call(inputs)
        if return_aux_features:
            return out, self._aux_input_feats
        else:
            return out

    @property
    def aux_features(self) -> list:
        return self._aux_features
