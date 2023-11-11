
class ModelAnalyzer(Callback):
    def __init__(self, mode='backward'):
        """
        Args:
            mode: 'forward' 分析各层前向输出 or 'backward' 分析各层反向梯度
        """
        super().__init__()
        assert mode in ['forward', 'backward'], '`mode` must be "forward" or "backward"!'
        self.mode = mode

    def on_fit_start(self, trainer, pl_module):
        def output_stats(hook, module, inputs, outputs):
            if isinstance(outputs, tuple):  # backward hook
                outputs = outputs[0]
            hook.mean = outputs[0].data.mean()
            hook.std = outputs[0].data.std()
            hook.data = outputs[0].data
        self.hooks = Hooks(pl_module.model, output_stats, self.mode)

    def on_train_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        mode = 'FORWARD' if self.mode == 'forward' else 'BACKWARD'
        mean_dict = {h.name: h.mean for h in self.hooks}
        std_dict = {h.name: h.std for h in self.hooks}
        logger = pl_module.logger.experiment
        logger.add_scalars(f'{mode}-mean', mean_dict, global_step=pl_module.global_step)
        logger.add_scalars(f'{mode}-std', std_dict, global_step=pl_module.global_step)
        for h in self.hooks:
            logger.add_histogram(f'{mode}-{h.name}', h.data, global_step=pl_module.global_step)

    def on_fit_end(self, trainer, pl_module):
        self.hooks.remove()
