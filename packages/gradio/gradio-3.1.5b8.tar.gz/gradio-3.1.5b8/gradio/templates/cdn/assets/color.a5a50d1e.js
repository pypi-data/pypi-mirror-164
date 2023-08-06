import { ae as ordered_colors } from './index.8a7211f1.js';

const get_next_color = (index) => {
  return ordered_colors[index % ordered_colors.length];
};

export { get_next_color as g };
