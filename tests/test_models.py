import keras_resnet.models


class TestResNet18:
    def test_constructor(self, x):
        model = keras_resnet.models.ResNet18(x)

        assert len(model.layers) == 88


class TestResNet34:
    def test_constructor(self, x):
        model = keras_resnet.models.ResNet34(x)

        assert len(model.layers) == 160


class TestResNet50:
    def test_constructor(self, x):
        model = keras_resnet.models.ResNet50(x)

        assert len(model.layers) == 192


class TestResNet101:
    def test_constructor(self, x):
        model = keras_resnet.models.ResNet101(x)

        assert len(model.layers) == 379


class TestResNet152:
    def test_constructor(self, x):
        model = keras_resnet.models.ResNet152(x)

        assert len(model.layers) == 566


class TestResNet200:
    def test_constructor(self, x):
        model = keras_resnet.models.ResNet200(x)

        assert len(model.layers) == 742
