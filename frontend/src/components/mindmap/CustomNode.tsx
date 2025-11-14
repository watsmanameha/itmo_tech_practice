import React, { memo } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';

interface CustomNodeData {
  label: string;
  isCenter?: boolean;
  isHighlighted?: boolean;
  onMouseEnter?: (id: string) => void;
  onMouseLeave?: () => void;
}

const CustomNode: React.FC<NodeProps<CustomNodeData>> = ({ data, id }) => {
  const isCenter = data.isCenter || false;
  const isHighlighted = data.isHighlighted || false;

  return (
    <div
      onMouseEnter={() => data.onMouseEnter?.(id)}
      onMouseLeave={() => data.onMouseLeave?.()}
      className={`px-4 py-2 rounded-lg border-2 shadow-md transition-all ${
        isCenter
          ? 'bg-gray-900 text-white border-gray-900 font-semibold'
          : isHighlighted
          ? 'bg-primary-50 text-gray-900 border-primary-500 scale-105'
          : 'bg-white text-gray-900 border-gray-300'
      }`}
      style={{
        minWidth: '150px',
        maxWidth: '250px',
      }}
    >
      <Handle
        type="target"
        position={Position.Top}
        className="w-3 h-3 bg-primary-500"
      />
      <div className="text-center text-sm">{data.label}</div>
      <Handle
        type="source"
        position={Position.Bottom}
        className="w-3 h-3 bg-primary-500"
      />
    </div>
  );
};

export default memo(CustomNode);
