def classFactory(iface):  # pylint: disable=invalid-name
    """
    QGISがプラグインを取得するために呼び出す関数
    """

    from .sample_plugin import SamplePlugin

    return SamplePlugin(iface)
